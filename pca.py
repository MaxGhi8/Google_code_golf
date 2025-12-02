import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Sequence, Dict, Any

import numpy as np


DATA_PATH = Path(__file__).parent / "inputs" / "task048.json"


def load_task(path: Path) -> Tuple[List[List[List[int]]], List[int]]:
	with open(path, "r") as f:
		obj = json.load(f)

	def to_xy(split: Sequence[dict]):
		X, y = [], []
		for ex in split:
			X.append(ex["input"])  # list[list[int]]
			out = ex["output"]
			# Outputs are [[0]] or [[8]]; map to 0/1 label (1 for 8)
			y.append(1 if (isinstance(out, list) and out and isinstance(out[0], list) and out[0] and out[0][0] == 8) else 0)
		return X, y

	X_tr, y_tr = to_xy(obj.get("train", []))
	X_te, y_te = to_xy(obj.get("test", []))
	X_ag, y_ag = to_xy(obj.get("arc-gen", []))

	X = X_tr + X_te + X_ag
	y = y_tr + y_te + y_ag
	return X, y


def max_shape(mats: Sequence[Sequence[Sequence[int]]]) -> Tuple[int, int]:
	h = max(len(m) for m in mats)
	w = max(len(m[0]) for m in mats)
	return h, w


def pad_to_shape(m: Sequence[Sequence[int]], H: int, W: int, pad_val: int = 0) -> np.ndarray:
	a = np.full((H, W), pad_val, dtype=np.int16)
	mh, mw = len(m), len(m[0])
	a[:mh, :mw] = np.array(m, dtype=np.int16)
	return a


def build_matrix_dataset(mats: List[List[List[int]]]) -> Tuple[np.ndarray, Tuple[int, int]]:
	H, W = max_shape(mats)
	X = np.stack([pad_to_shape(m, H, W) for m in mats], axis=0)
	return X, (H, W)


def center(X: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
	mu = X.mean(axis=0)
	return X - mu, mu


def pca_svd(X: np.ndarray, k: int = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
	# X shape: n_samples x n_features, centered
	U, S, Vt = np.linalg.svd(X, full_matrices=False)
	if k is not None:
		U, S, Vt = U[:, :k], S[:k], Vt[:k, :]
	# components_: k x d (like sklearn) rows are principal axes
	return U, S, Vt


def explained_variance_ratio(S: np.ndarray, n_samples: int) -> np.ndarray:
	# singular values S relate to eigenvalues of covariance: eig = S^2 / (n-1)
	eig = (S ** 2) / max(n_samples - 1, 1)
	return eig / eig.sum()


def pixel_correlations(X: np.ndarray, y: np.ndarray) -> np.ndarray:
	# Pearson correlation between each feature column and y
	y_centered = y - y.mean()
	Xc = X - X.mean(axis=0)
	num = (Xc * y_centered[:, None]).sum(axis=0)
	denom = np.sqrt((Xc ** 2).sum(axis=0)) * math.sqrt((y_centered ** 2).sum())
	with np.errstate(divide="ignore", invalid="ignore"):
		r = np.where(denom == 0, 0.0, num / denom)
	return r


def evaluate_subset_rule(X: np.ndarray, y: np.ndarray, idxs: List[int]) -> Tuple[float, float, float]:
	# Simple rule: sum selected pixel intensities > threshold -> class 1 (8), else 0
	if len(idxs) == 0:
		return 0.0, 0.0, 0.0
	s = X[:, idxs].sum(axis=1)
	# Candidate thresholds: midpoints between sorted unique sums
	uniq = np.unique(s)
	if len(uniq) == 1:
		thr = uniq[0] + 0.5
		pred = (s > thr).astype(int)
		acc = (pred == y).mean()
		return acc, thr, 1.0
	# Try thresholds between consecutive values and also below/above range
	cands = []
	cands.append(uniq[0] - 1)
	for a, b in zip(uniq[:-1], uniq[1:]):
		cands.append((a + b) / 2.0)
	cands.append(uniq[-1] + 1)
	best = (-1.0, 0.0, 1.0)  # acc, thr, polarity
	for thr in cands:
		for pol in (1.0, -1.0):  # allow flipping inequality
			pred = (pol * s > pol * thr).astype(int)
			acc = (pred == y).mean()
			if acc > best[0]:
				best = (acc, thr, pol)
	return best


# ----- Non-linear rule search -----

@dataclass(frozen=True)
class Feature:
	name: str  # expression string, e.g., x[2][3]
	values: np.ndarray  # shape (n,)
	kind: str  # 'raw' | 'eq8' | 'eq2' | 'nz' | 'prod'
	meta: Tuple[Any, ...]  # e.g., ((r,c),) or ((r1,c1),(r2,c2))


def gen_feature_pool(X_img: np.ndarray, top_raw: int = 24, top_eq8: int = 24, prod_from_raw: int = 12) -> List[Feature]:
	n, h, w = X_img.shape
	d = h * w
	X = X_img.reshape(n, d).astype(np.int16)

	# Rank indices by correlation to y using raw pixels after we get y in outer scope; we'll compute here with a proxy:
	# We'll return raw features first, actual ranking will be done externally where y is available.
	feats: List[Feature] = []
	# Raw pixel features
	for j in range(d):
		r, c = divmod(j, w)
		vals = X[:, j].astype(np.float32)
		feats.append(Feature(name=f"x[{r}][{c}]", values=vals, kind="raw", meta=((r, c),)))
	# Boolean flags per pixel
	eq8: List[Feature] = []
	eq2: List[Feature] = []
	nz: List[Feature] = []
	for j in range(d):
		r, c = divmod(j, w)
		v = X[:, j]
		eq8.append(Feature(name=f"(x[{r}][{c}]>7)", values=(v == 8).astype(np.float32), kind="eq8", meta=((r, c),)))
		eq2.append(Feature(name=f"(x[{r}][{c}]==2)", values=(v == 2).astype(np.float32), kind="eq2", meta=((r, c),)))
		nz.append(Feature(name=f"(x[{r}][{c}]>0)", values=(v > 0).astype(np.float32), kind="nz", meta=((r, c),)))
	# We'll select top_eq8 later; for now, return all and let the selector prune.
	# Products will also be selected from top raw later.
	return feats + eq8 + eq2 + nz


def rank_features(features: List[Feature], y: np.ndarray) -> List[int]:
	# Rank by absolute Pearson correlation with y; break ties by variance and shorter name
	ys = y.astype(np.float32)
	yc = ys - ys.mean()
	yden = math.sqrt(float((yc * yc).sum())) or 1.0
	scores = []
	for i, f in enumerate(features):
		v = f.values
		vc = v - v.mean()
		vden = math.sqrt(float((vc * vc).sum())) or 1.0
		corr = float((vc * yc).sum()) / (vden * yden)
		var = float(vden)
		scores.append((abs(corr), var, -len(f.name), i))
	scores.sort(reverse=True)
	return [i for (_, _, _, i) in scores]


def build_products(features: List[Feature], ranked_raw_idxs: List[int], X_img: np.ndarray, max_raw_for_prod: int, max_pairs: int = 100) -> List[Feature]:
	n, h, w = X_img.shape
	# Filter raw features from ranked list
	raw_idxs = [i for i in ranked_raw_idxs if features[i].kind == "raw"][:max_raw_for_prod]
	prods: List[Feature] = []
	# Limit pair count
	count = 0
	for a_idx, i in enumerate(raw_idxs):
		vi = features[i]
		for j in raw_idxs[a_idx + 1:]:
			vj = features[j]
			vals = (vi.values * vj.values).astype(np.float32)
			# Skip constant features
			if vals.max() == vals.min():
				continue
			name = f"({vi.name}*{vj.name})"
			prods.append(Feature(name=name, values=vals, kind="prod", meta=(vi.meta[0], vj.meta[0])))
			count += 1
			if count >= max_pairs:
				return prods
	return prods


def best_threshold_for_scores(s: np.ndarray, y: np.ndarray) -> Tuple[float, float, float]:
	# same as in evaluate_subset_rule but generalized to any score vector s
	uniq = np.unique(s)
	if len(uniq) == 1:
		thr = uniq[0] + 0.5
		pred = (s > thr).astype(int)
		acc = float((pred == y).mean())
		return acc, float(thr), 1.0
	cands = []
	cands.append(uniq[0] - 1)
	for a, b in zip(uniq[:-1], uniq[1:]):
		cands.append((float(a) + float(b)) / 2.0)
	cands.append(uniq[-1] + 1)
	best = (-1.0, 0.0, 1.0)
	for thr in cands:
		for pol in (1.0, -1.0):
			pred = (pol * s > pol * thr).astype(int)
			acc = float((pred == y).mean())
			if acc > best[0]:
				best = (acc, float(thr), float(pol))
	return best


def beam_search(features: List[Feature], y: np.ndarray, beam_width: int = 120, max_k: int = 6, weights: Tuple[int, ...] = (-2, -1, 1, 2)):
	n = len(y)
	# Build matrix for fast additions
	F = np.stack([f.values for f in features], axis=1).astype(np.float32)  # n x m

	# Initialize beam with single-feature models
	BeamState = Dict[str, Any]
	beam = []  # type: List[Dict[str, Any]]
	for j in range(F.shape[1]):
		col = F[:, j]
		for w in weights:
			s = w * col
			acc, thr, pol = best_threshold_for_scores(s, y)
			beam.append({
				"idxs": (j,),
				"weights": (w,),
				"s": s,
				"acc": acc,
				"thr": thr,
				"pol": pol,
			})
	# Keep best
	beam.sort(key=lambda b: (b["acc"], -len(b["idxs"])) , reverse=True)
	beam = beam[:beam_width]

	best = max(beam, key=lambda b: b["acc"]) if beam else None
	if best and best["acc"] == 1.0:
		return best

	m = F.shape[1]
	for k in range(2, max_k + 1):
		next_beam = []  # type: List[Dict[str, Any]]
		seen = set()
		for b in beam:
			used = set(b["idxs"])
			base_s = b["s"]
			for j in range(m):
				if j in used:
					continue
				col = F[:, j]
				for w in weights:
					s = base_s + w * col
					acc, thr, pol = best_threshold_for_scores(s, y)
					idxs = tuple(sorted(b["idxs"] + (j,)))
					# Instead, maintain parallel arrays; recompute:
					# We'll reconstruct weights by aligning order of idxs: use a dict
					prev_pairs = list(zip(b["idxs"], b["weights"]))
					weight_map = {ii: ww for ii, ww in prev_pairs}
					weight_map[j] = w
					idxs_sorted = tuple(sorted(weight_map.keys()))
					weights_sorted = tuple(weight_map[i] for i in idxs_sorted)
					key = (idxs_sorted, weights_sorted)
					if key in seen:
						continue
					seen.add(key)
					next_beam.append({
						"idxs": idxs_sorted,
						"weights": weights_sorted,
						"s": s,
						"acc": acc,
						"thr": thr,
						"pol": pol,
					})
		if not next_beam:
			break
		next_beam.sort(key=lambda b: (b["acc"], -len(b["idxs"])) , reverse=True)
		beam = next_beam[:beam_width]
		best = max(beam, key=lambda b: b["acc"]) if beam else best
		if best and best["acc"] == 1.0:
			return best
	return best


def evaluate_s_vector(s: np.ndarray, y: np.ndarray) -> Tuple[float, float, float]:
	# Given precomputed scores s, find best threshold and polarity
	uniq = np.unique(s)
	if len(uniq) == 1:
		thr = uniq[0] + 0.5
		pred = (s > thr).astype(int)
		acc = (pred == y).mean()
		return acc, thr, 1.0
	cands = [uniq[0] - 1]
	for a, b in zip(uniq[:-1], uniq[1:]):
		cands.append((a + b) / 2.0)
	cands.append(uniq[-1] + 1)
	best = (-1.0, 0.0, 1.0)
	for thr in cands:
		for pol in (1.0, -1.0):
			pred = (pol * s > pol * thr).astype(int)
			acc = (pred == y).mean()
			if acc > best[0]:
				best = (acc, thr, pol)
	return best


def corr_columns(F: np.ndarray, y: np.ndarray) -> np.ndarray:
	# Correlation of each feature column with label y
	y_centered = y - y.mean()
	Fc = F - F.mean(axis=0)
	num = (Fc * y_centered[:, None]).sum(axis=0)
	denom = np.sqrt((Fc ** 2).sum(axis=0)) * math.sqrt((y_centered ** 2).sum())
	with np.errstate(divide="ignore", invalid="ignore"):
		r = np.where(denom == 0, 0.0, num / denom)
	return r


def feature_matrix(X: np.ndarray, kind: str) -> np.ndarray:
	if kind == "raw":
		return X.copy()
	if kind == "is8":
		return (X == 8).astype(np.int16)
	if kind == "is2":
		return (X == 2).astype(np.int16)
	if kind == "nz":
		return (X > 0).astype(np.int16)
	if kind == "is0":
		return (X == 0).astype(np.int16)
	if kind == "p82":  # 8->1, 2->-1, else 0
		a = np.zeros_like(X, dtype=np.int16)
		a[X == 8] = 1
		a[X == 2] = -1
		return a
	if kind == "p80":  # 8->1, 0->-1, else 0
		a = np.zeros_like(X, dtype=np.int16)
		a[X == 8] = 1
		a[X == 0] = -1
		return a
	raise ValueError(f"unknown feature kind: {kind}")


def beam_search_perfect_rule(
	X: np.ndarray,
	y: np.ndarray,
	kind: str,
	pool_size: int = 30,
	max_k: int = 7,
	beam_width: int = 200,
) -> Tuple[float, List[int], List[int], float, float]:
	# Returns acc, idxs, weights, thr, pol
	F = feature_matrix(X, kind)  # n x d
	n, d = F.shape
	# Rank candidate indices by |corr|
	r = corr_columns(F, y)
	cand = list(np.argsort(-np.abs(r))[:min(pool_size, d)])

	# Beam states: (idxs_tuple, weights_tuple, s_vector)
	beams = []
	for j in cand:
		for w in (1, -1):
			s = w * F[:, j]
			acc, thr, pol = evaluate_s_vector(s, y)
			if acc == 1.0:
				return acc, [j], [w], thr, pol
			beams.append(({j}, (j,), (w,), s, acc, thr, pol))

	# Keep top beams
	beams.sort(key=lambda t: (-t[5], len(t[1])))
	beams = beams[:beam_width]

	for depth in range(2, max_k + 1):
		next_beams = []
		seen = set()
		for st in beams:
			idx_set, idxs, ws, s, acc, thr, pol = st
			for j in cand:
				if j in idx_set:
					continue
				for w in (1, -1):
					idxs2 = idxs + (j,)
					ws2 = ws + (w,)
					key = (idxs2, ws2)
					if key in seen:
						continue
					seen.add(key)
					s2 = s + w * F[:, j]
					acc2, thr2, pol2 = evaluate_s_vector(s2, y)
					if acc2 == 1.0:
						return acc2, list(idxs2), list(ws2), thr2, pol2
					next_beams.append((idx_set | {j}, idxs2, ws2, s2, acc2, thr2, pol2))

		if not next_beams:
			break
		next_beams.sort(key=lambda t: (-t[4], len(t[1])))
		beams = next_beams[:beam_width]

	# Return best encountered if perfect not found
	best = max(beams, key=lambda t: t[4]) if beams else None
	if best is None:
		return 0.0, [], [], 0.0, 1.0
	_, idxs, ws, _, acc, thr, pol = best
	return acc, list(idxs), list(ws), thr, pol


def build_general_features(X_img: np.ndarray) -> Tuple[np.ndarray, List[str]]:
	"""Build a wider feature set and the corresponding expression strings.
	Includes raw pixels, boolean indicators, row/col sums, 2x2 block sums,
	and pairwise products among top-correlated raw and is8 pixels.
	"""
	n, h, w = X_img.shape
	X = X_img.reshape(n, h * w).astype(np.float32)
	exprs: List[str] = []
	cols: List[np.ndarray] = []

	# raw
	for j in range(h * w):
		r, c = divmod(j, w)
		cols.append(X[:, j])
		exprs.append(f"x[{r}][{c}]")

	# booleans: ==8, ==2, ==0, >0
	eq8 = (X == 8).astype(np.float32)
	eq2 = (X == 2).astype(np.float32)
	eq0 = (X == 0).astype(np.float32)
	nz = (X > 0).astype(np.float32)
	for j in range(h * w):
		r, c = divmod(j, w)
		cols.append(eq8[:, j]); exprs.append(f"(x[{r}][{c}]==8)")
		cols.append(eq2[:, j]); exprs.append(f"(x[{r}][{c}]==2)")
		cols.append(eq0[:, j]); exprs.append(f"(x[{r}][{c}]==0)")
		cols.append(nz[:, j]);  exprs.append(f"(x[{r}][{c}]>0)")

	# row sums and column sums (raw)
	row_sums = X_img.sum(axis=2)  # n x h
	for r in range(h):
		cols.append(row_sums[:, r].astype(np.float32))
		exprs.append(f"sum(x[{r}])")
	col_sums = X_img.sum(axis=1)  # n x w
	for c in range(w):
		cols.append(col_sums[:, c].astype(np.float32))
		exprs.append(f"sum(r[{c}]for r in x)")

	# 2x2 block sums
	for r in range(h - 1):
		for c in range(w - 1):
			block = X_img[:, r:r+2, c:c+2].sum(axis=(1, 2)).astype(np.float32)
			cols.append(block)
			exprs.append(f"x[{r}][{c}]+x[{r}][{c+1}]+x[{r+1}][{c}]+x[{r+1}][{c+1}]")

	# Pairwise products among top-correlated raw and is8
	# Rank raw by corr
	r_vec = pixel_correlations(X, (X == 8).sum(axis=1) > 0)  # rough proxy; will filter by y later anyway
	order_raw = np.argsort(-np.abs(r_vec))[:20]
	for i in range(len(order_raw)):
		a = order_raw[i]
		ra, ca = divmod(a, w)
		for j in range(i + 1, len(order_raw)):
			b = order_raw[j]
			rb, cb = divmod(b, w)
			prod = (X[:, a] * X[:, b]).astype(np.float32)
			cols.append(prod)
			exprs.append(f"x[{ra}][{ca}]*x[{rb}][{cb}]")

	order_is8 = np.argsort(-np.abs(pixel_correlations(eq8, eq8.sum(axis=1))))[:20]
	for i in range(len(order_is8)):
		a = order_is8[i]
		ra, ca = divmod(a % (h * w), w)
		for j in range(i + 1, len(order_is8)):
			b = order_is8[j]
			rb, cb = divmod(b % (h * w), w)
			prod = (eq8[:, a % (h * w)] * eq8[:, b % (h * w)]).astype(np.float32)
			cols.append(prod)
			exprs.append(f"(x[{ra}][{ca}]==8)*(x[{rb}][{cb}]==8)")

	F = np.stack(cols, axis=1)
	return F, exprs


def beam_search_perfect_rule_general(
	F: np.ndarray,
	exprs: List[str],
	y: np.ndarray,
	pool_size: int = 256,
	max_k: int = 8,
	beam_width: int = 4000,
	weights: Sequence[int] = (-2, -1, 1, 2),
):
	# Rank by correlation with label
	r = corr_columns(F, y)
	order = np.argsort(-np.abs(r))[:min(pool_size, F.shape[1])]
	n = F.shape[0]

	def best_thr(s: np.ndarray):
		return evaluate_s_vector(s, y)

	beams = []
	best = None
	for j in order:
		col = F[:, j].astype(np.float32)
		for wgt in weights:
			s = wgt * col
			acc, thr, pol = best_thr(s)
			if best is None or acc > best[0]:
				best = (acc, [(j, wgt)], thr, pol, s)
			if acc == 1.0:
				return {
					"acc": 1.0,
					"terms": [(j, wgt)],
					"expr": f"{wgt}*({exprs[j]})" if wgt not in (1, -1) else (exprs[j] if wgt == 1 else f"-({exprs[j]})"),
					"threshold": float(thr),
					"cmp": ">" if pol > 0 else "<",
					"golf": f"(({exprs[j] if wgt==1 else ('-('+exprs[j]+')' if wgt==-1 else str(wgt)+'*('+exprs[j]+')')}) {'>' if pol>0 else '<'} {int(thr) if float(thr).is_integer() else thr:.2f}) and 8 or 0",
				}
			beams.append((acc, s, [(j, wgt)]))
	beams.sort(key=lambda t: t[0], reverse=True)
	beams = beams[:beam_width]

	for depth in range(2, max_k + 1):
		next_beams = []
		seen = set()
		for acc0, s0, terms0 in beams:
			used = {j for j, _ in terms0}
			for j in order:
				if j in used:
					continue
				col = F[:, j].astype(np.float32)
				for wgt in weights:
					terms = terms0 + [(j, wgt)]
					key = tuple(terms)
					if key in seen:
						continue
					seen.add(key)
					s = s0 + wgt * col
					acc, thr, pol = best_thr(s)
					if best is None or acc > best[0]:
						best = (acc, terms, thr, pol, s)
					if acc == 1.0:
						# Build expr
						parts = []
						for jj, ww in terms:
							e = exprs[jj]
							if ww == 1:
								parts.append(e)
							elif ww == -1:
								parts.append(f"-({e})")
							else:
								parts.append(f"{ww}*({e})")
						sum_expr = "+".join(parts) if parts else "0"
						cmp_op = ">" if pol > 0 else "<"
						thr_out = float(thr)
						golf = f"(({sum_expr}) {cmp_op} {int(thr_out) if float(thr_out).is_integer() else thr_out:.2f}) and 8 or 0"
						return {
							"acc": 1.0,
							"terms": terms,
							"expr": sum_expr,
							"threshold": thr_out,
							"cmp": cmp_op,
							"golf": golf,
						}
					next_beams.append((acc, s, terms))
		if not next_beams:
			break
		next_beams.sort(key=lambda t: t[0], reverse=True)
		beams = next_beams[:beam_width]

	if best is None:
		return {"acc": 0.0}
	acc, terms, thr, pol, _ = best
	parts = []
	for jj, ww in terms:
		e = exprs[jj]
		if ww == 1:
			parts.append(e)
		elif ww == -1:
			parts.append(f"-({e})")
		else:
			parts.append(f"{ww}*({e})")
	sum_expr = "+".join(parts) if parts else "0"
	cmp_op = ">" if pol > 0 else "<"
	thr_out = float(thr)
	golf = f"(({sum_expr}) {cmp_op} {int(thr_out) if float(thr_out).is_integer() else thr_out:.2f}) and 8 or 0"
	return {
		"acc": float(acc),
		"terms": terms,
		"expr": sum_expr,
		"threshold": thr_out,
		"cmp": cmp_op,
		"golf": golf,
	}


def main() -> None:
	X_mats, y_list = load_task(DATA_PATH)
	X_img, (H, W) = build_matrix_dataset(X_mats)
	y = np.array(y_list, dtype=np.int8)

	n, h, w = X_img.shape
	print(f"Dataset size: {n}, padded shape: {h}x{w}")

	# Build initial pool (raw + boolean flags)
	all_feats = gen_feature_pool(X_img)
	ranked = rank_features(all_feats, y)
	# Select top subsets for raw and eq8 kinds to limit search size
	# Get indices by kind
	raw_idxs = [i for i in ranked if all_feats[i].kind == "raw"][:24]
	eq8_idxs = [i for i in ranked if all_feats[i].kind == "eq8"][:24]
	# Build product features among top raw
	prods = build_products(all_feats, raw_idxs, X_img, max_raw_for_prod=12, max_pairs=80)
	# Assemble final feature list
	features = [all_feats[i] for i in raw_idxs + eq8_idxs] + prods

	# Re-rank final features against y for better beam starting order
	final_rank = rank_features(features, y)
	features = [features[i] for i in final_rank]

	# Run beam search
	best = beam_search(features, y, beam_width=120, max_k=6, weights=(-2, -1, 1, 2))
	if not best:
		print("No model found.")
		return
	acc = best["acc"]
	thr = best["thr"]
	pol = best["pol"]
	idxs = best["idxs"]
	weights = best["weights"]

	# Build expression
	terms = []
	for j, wgt in zip(idxs, weights):
		name = features[j].name
		if wgt == 1:
			terms.append(name)
		elif wgt == -1:
			terms.append(f"-{name}")
		else:
			terms.append(f"{wgt}*{name}")
	expr = "+".join(terms).replace("+-", "-")
	cmp_str = ">" if pol > 0 else "<"

	print("Best model:")
	print(f"  acc={acc:.3f}, k={len(idxs)}, thr={thr:.2f}, pol={pol:+.0f}")
	print("  terms:", terms)
	print("\nGolf hint (Python-ish):")
	print(f"  (({expr}) {cmp_str} {thr:.0f}) and 8 or 0")

	# Try to find a perfect rule with a small subset using simple features
	print("\nSearching for perfect rule with tiny subset (beam search)...")
	# Prepare flattened X for simple feature kinds
	X = X_img.reshape(n, h * w).astype(np.int16)
	best_any = None
	for kind in ("p82", "p80", "is8", "nz", "raw", "is2", "is0"):
		acc_b, idxs_b, ws_b, thr_b, pol_b = beam_search_perfect_rule(X, y, kind, pool_size=64, max_k=12, beam_width=5000)
		if best_any is None or acc_b > best_any[0]:
			best_any = (acc_b, kind, idxs_b, ws_b, thr_b, pol_b)
		print(f"  {kind}: acc={acc_b:.3f}, k={len(idxs_b)}, thr={thr_b:.2f}, pol={pol_b:+.0f}, idxs={idxs_b}, ws={ws_b}")
		if acc_b == 1.0:
			break

	if best_any and best_any[0] == 1.0:
		_, kind, idxs_b, ws_b, thr_b, pol_b = best_any
		coords_b = [divmod(j, w) for j in idxs_b]
		print("\nPerfect rule found:")
		print(f"  feature={kind}, k={len(idxs_b)}, thr={thr_b:.2f}, pol={pol_b:+.0f}")
		print(f"  indices={idxs_b}, weights={ws_b}")
		print(f"  coords={coords_b}")
		# Golf hint
		if pol_b > 0:
			cmp_str = ">"
		else:
			cmp_str = "<"
		def term_str(kind: str, r: int, c: int) -> str:
			if kind == "raw":
				return f"x[{r}][{c}]"
			if kind == "is8":
				return f"(x[{r}][{c}]==8)"
			if kind == "is2":
				return f"(x[{r}][{c}]==2)"
			if kind == "nz":
				return f"(x[{r}][{c}]>0)"
			return f"x[{r}][{c}]"
		pieces = []
		for (r0, c0), w0 in zip(coords_b, ws_b):
			t = term_str(kind, int(r0), int(c0))
			if w0 == -1:
				pieces.append(f"-{t}")
			else:
				pieces.append(t)
		expr = "+".join(pieces) if pieces else "0"
		print("Golf hint:")
		print(f"  (({expr}) {cmp_str} {thr_b:.0f}) and 8 or 0")
	else:
		print("\nNo perfect rule found within the simple-feature search. Trying general feature set...")
		F, exprs = build_general_features(X_img)
		rule = beam_search_perfect_rule_general(F, exprs, y, pool_size=512, max_k=8, beam_width=6000, weights=(-3, -2, -1, 1, 2, 3))
		print(f"General beam result acc={rule.get('acc', 0):.3f}")
		if rule.get("acc") == 1.0:
			print("Perfect rule (general):")
			print("Expr:", rule["expr"])
			print(f"Compare: {rule['cmp']} {rule['threshold']}")
			print("Golf:", rule["golf"])
		else:
			print("No perfect rule found in general set either. Consider increasing search limits or adding more atoms.")


if __name__ == "__main__":
	main()

