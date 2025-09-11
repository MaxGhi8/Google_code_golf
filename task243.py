def p(g):
 n=len(g);L=sum(g,[])
 def f(i,j):
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if n>(x:=i+x)>-1<(y:=j+y)<n and g[x][y]<1:g[x][y]|=1;f(x,y)
 [f(i//n,i%n)for i in range(n*n)if L[i]==1];return g