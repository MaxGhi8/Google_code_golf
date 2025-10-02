def p(g):
 for x in range(121):
  y=x%11;x//=11
  for i in range(12-x):
   t=g[x:x+i];z=y+i
   if all(g[x-1][y:z]+g[x+i][y:z]+[v[z:]and v[y-1]&v[z]and 5not in v[y:z]for v in t]):
    for v in t:v[y:z]=[2]*i
 return g