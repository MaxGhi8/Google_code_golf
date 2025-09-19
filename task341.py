def p(g):
 for _ in'  ':
  *g,=map(list,zip(*g))
  for r in[r for r in g if len({*r})>2][1:-1]:
   for j in range(10):r[j]=r[j]or(1<len({*r[j:]})<3)*8
 return g