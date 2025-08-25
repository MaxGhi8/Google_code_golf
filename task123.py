def p(g,R=range(10)):
 g=[r[:1]*10for r in g*3if r[0]]
 for r in R:
  for c in R:g[r][c]=g[c][r]
 return g[:10]