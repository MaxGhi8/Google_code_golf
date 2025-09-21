def p(g):
 s=sum(g,[]);a,b,*_=sorted({*s},key=s.count);w=len(g[0]);h=len(g)
 def f(i,j):
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if h>(x:=i+x)>-1<(y:=j+y)<w and g[x][y]<1:g[x][y]=g[i][j]^a^b;f(x,y)
 for k in range(w*h):s[k]&7and f(k//w,k%w)
 return g