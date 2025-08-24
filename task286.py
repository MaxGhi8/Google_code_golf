def p(g):
 a,b,*_=sorted({*(s:=sum(g,[]))},key=s.count);w=len(g[0])
 def f(i,j):
  for x,y in[1,0],[-1,0],[0,1],[0,-1]:
   if-1<(I:=i+x)<len(g)and-1<(J:=j+y)<w and g[I][J]<1:g[I][J]=g[i][j]^a^b;f(I,J)
 for k,v in enumerate(s):
  if 0<v!=8:f(*divmod(k,w))
 return g