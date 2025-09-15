def p(g,R=range(10)):
 def f(i,j,m):
  k=1;m[i][j]=5
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if 10>(x:=i+x)>-1<(y:=j+y)<10 and m[x][y]<1:k+=f(x,y,m)
  return k
 return[[g[i][j]or 4-f(i,j,[*map(list,g)])for j in R]for i in R]