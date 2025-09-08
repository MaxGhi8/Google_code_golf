def p(g,R=range(10)):
 for k in R:
  for j in[*R]*(g[-1][k]>0):
   if g[~j][k]>2:k+=1;g[-j][k]=2
   g[~j][k]=2
 return g