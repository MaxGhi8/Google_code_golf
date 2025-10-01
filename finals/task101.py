def p(g,t=[],E=enumerate):
 def b(z):
  if z in P:C[z]=P.pop(z);x,y=z;b((x-1,y));b((x+1,y));b((x,y-1));b((x,y+1))
 for _ in' '*3:
  P,*S={(r,c):v for r,G in E(g)for c,v in E(G)if v},
  while P:S+=[C:={}];b([*P][0]);x=0
  for C in S:r,c=min(z for z in C if C[z]>1);1in C.values()and(t or(t:=[(a-r,b-c)for a,b in C if C[a,b]<2]))or(x or(x:=(C,r,c)))
  if x:
   C,r,c=x;M=min(3,int(len(C)**.5))
   for u,v in t:
    for i in range(M*M):g[r+u*M+i//M][max(0,c+v*M+i%M)]=1
 return g