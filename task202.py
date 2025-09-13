def p(g,e=enumerate):
 for _ in'  ':
  g=[*map(list,zip(*g))]
  for i,r in e(g*(len({*g[0]}-{0})>1)):
   for j,v in e(r):r[j]=[v,0][0 in r and v in{x[r.index(0)]for x in g[i-3:]}]
 return g