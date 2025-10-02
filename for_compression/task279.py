def p(g,E=enumerate):
 def f(i,j,a,b,k):
  k|={(i,j)}
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if len(g)>(x:=i+x)>-1<(y:=j+y)<len(g[0])and 2>g[x][y]and(x-a|y-b)and((x,y)in k or f(x,y,i,j,k)):return 7
  return 0
 return[[v+f(i,j,-1,-1,set())*(2>v)for j,v in E(r)]for i,r in E(g)]