def p(g,R=range(10)):
 def f(i,j):
  g[i][j]=3;k=1+sum(f(x,y)for x,y in((i+1,j),(i-1,j),(i,j+1),(i,j-1))if 0<=x<10>y>=0<g[x][y]//5);g[i][j]=5;return k
 return[[g[i][j]and[2,4,1][sum(s<f(i,j)for s in{f(i,j)for i in R for j in R if g[i][j]})]for j in R]for i in R]