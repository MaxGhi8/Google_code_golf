def p(g,R=range(10)):
 def f(i,j):
  k=1;g[i][j]=3
  for x,y in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
   if 10>x>-1<y<10and g[x][y]>4:k+=f(x,y)
  g[i][j]=5;return k
 return[[[2,4,1][sorted({f(i,j)for i in R for j in R if g[i][j]}).index(f(i,j))]if g[i][j]else 0for j in R]for i in R]