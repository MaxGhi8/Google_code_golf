def p(g):
 for _ in[0]*4:
  g=[*zip(*g)][::-1];D={v:i for i,r in enumerate(g)for v in[2,8]if v in r};a=D[8]
  if a<D[2]and 2not in g[a]:g=(g[:a+1]+[r for r in g if 2in r]+[[0]*len(g[0])]*99)[:len(g)]
 return g