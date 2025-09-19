def p(g,R=range(10)):
 def f(i,j,m):
  m[i][j]=1
  return 1+sum((10>(x:=i+a)>-1<(y:=j+b)<10 and m[x][y]<1 and f(x,y,m))for a,b in((1,0),(-1,0),(0,1),(0,-1)))
 return[[g[i][j]or 4-f(i,j,[*map(list,g)])for j in R]for i in R]