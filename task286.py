def p(g,E=enumerate):
 a,b,*_=sorted({*(s:=sum(g,[]))},key=s.count)
 def f(i,j):
  for d in[1,0],[-1,0],[0,1],[0,-1]:
   if-1<(I:=i+d[0])<len(g)and-1<(J:=j+d[1])<len(g[0])and g[I][J]<1:g[I][J]=g[i][j]^a^b;f(I,J)
 for i,r in E(g):
  for j,v in E(r):
   if 0<v!=8:f(i,j)
 return g