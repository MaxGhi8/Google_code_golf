def p(g,E=enumerate):
 def f(i,j,a,b,k):
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if len(g)>(x:=i+x)>-1<(y:=j+y)<len(g[0])and(x,y)!=(a,b)and g[x][y]<2:
    if(x,y)in(k:=k|{(i,j)})or f(x,y,i,j,k):return 7
  return 0
 return[[v+f(i,j,-1,-1,set())*(v<2)for j,v in E(r)]for i,r in E(g)]