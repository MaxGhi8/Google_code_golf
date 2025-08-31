def p(g,v=[0,8,2],h=[0,6,7]):
 for I in range(100):
  if g[i:=I//10][j:=I%10]==1:
   for a in-1,1:
    if 0<=i+a<10:g[i+a][j]=v[a]
    if 0<=j+a<10:g[i][j+a]=h[a]
 return g