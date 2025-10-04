def p(g):
 for i,j in{(i,j)for i,r in enumerate(g)for j,x in enumerate(r)if x==5}:
  for a,b in(0,1),(0,-1),(1,0),(-1,0):
   u=x=i+a;v=y=j+b
   while-1<x<14 and-1<y<14 and g[x][y]-5:
    if g[x][y]%5:g[u][v]=5;g[x][y]*=x^u|y^v<1;u+=a;v+=b
    x+=a;y+=b
 return g