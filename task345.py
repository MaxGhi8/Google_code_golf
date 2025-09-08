def p(g,R=range(10)):
 for i in R:
  if g[-1][i]:
   c=0
   for j in R:
    if g[~j][i+c]>2:c+=1;g[-j][i+c]=2
    g[~j][i+c]=2
 return g