def p(g,E=enumerate):
 for j,r in E(g):
  for i,c in E(r):
   if c>4:
    for d in range(9):g[j-1+d//3][i-1+d%3]|=1
 return g