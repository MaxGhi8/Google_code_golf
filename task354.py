def p(g,R=range(10)):
 def d(i,j,v):
  if 0<=j<10>i>=0and g[i][j]==5:g[i][j]=v;d(i+1,j,v);d(i-1,j,v);d(i,j+1,v);d(i,j-1,v)
 [d(i,j,g[0][j])for i in R for j in R if g[i][j]==5and g[0][j]]
 return g