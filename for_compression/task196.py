def p(g):
 m,n=len(g),len(g[0])
 for a,b,c,d in[(a,b,c,d)for a in range(m)for b in range(n)for c in range(a+3,-~m)for d in range(b+3,-~n)if min(g[a][b:d]+g[c-1][b:d]+[r[b]*r[d-1]for r in g[a:c]])]:
  for r in g[a:c]:r[b]=r[d-1]=3;g[a][b:d]=g[c-1][b:d]=[3]*(d-b)
 return g