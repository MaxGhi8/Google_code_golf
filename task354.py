def p(g,R=range(10)):
 def d(i,j,v):
  if-1<i<10>j>-1and g[i][j]==5:g[i][j]=v;d(i+1,j,v);d(i-1,j,v);d(i,j+1,v);d(i,j-1,v)
 [d(i,j,v)for j in R if(v:=g[0][j])for i in R if g[i][j]==5]
 return g