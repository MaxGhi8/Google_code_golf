def p(g):
 for k in range(8):
  *g,=map(list,zip(*g[::-1]));g=g[:max(i+1for i,r in enumerate(g)if all(r))]
  for i,r in enumerate(g[2:-1]*(k>3)*(max(max(r[1:-1]for r in g[1:-1]))==g[-1][1]),2):r[:]=map(max,r,g[i-1])
 return g