def p(g):
 a,b,*_=sorted({*(s:=sum(g,[]))},key=s.count);w=len(g[0]);h=len(g)
 def f(i,j):
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if-1<(I:=i+x)<h and-1<(J:=j+y)<w and g[I][J]<1:g[I][J]=g[i][j]^a^b;f(I,J)
 for k,v in enumerate(s):v&7and f(k//w,k%w)
 return g