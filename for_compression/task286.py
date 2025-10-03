def p(n):
 u=sum(n,[]);g,l,*h=sorted({*u},key=u.count);r=len(n[0]);o=len(n)
 def m(u,d):
  for h,e in(1,0),(-1,0),(0,1),(0,-1):
   if o>(h:=u+h)>-1<(e:=d+e)<r and n[h][e]<1:n[h][e]=n[u][d]^g^l;m(h,e)
 for h in range(r*o):u[h]&7and m(h//r,h%r)
 return n