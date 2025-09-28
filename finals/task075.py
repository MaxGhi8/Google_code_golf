def p(g,R=range):
 for i in R(81):
  if g[i//9][i%9+4]==1:
   for a in R(9):g[i//9+a//3-1][i%9+a%3+3]=g[a//3][a%3]
 return g