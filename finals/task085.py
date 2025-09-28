def p(g):
 for a,b,c in zip(g,g[1:],g[2:]):
  if a==c:b[~b.index(max(b))%2::2]=[0]*(len(b)>>1)
 return g