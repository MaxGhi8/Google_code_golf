def p(g):
 for e,h,i in zip(g,g[1:],g[2:]):
  if e==i:h[~h.index(max(h))%2::2]=[0]*(len(h)>>1)
 return g