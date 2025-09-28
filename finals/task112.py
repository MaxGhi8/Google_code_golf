def p(g,E=enumerate):
 a,b=divmod(sum(g,[]).index(3),len(g[0]))
 for i,r in E(g):
  for j,v in E(r):
   if v==2:g[2*a+1-i][j]=r[2*b+1-j]=2
 return g