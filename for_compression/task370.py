def p(r,i=lambda r:[*zip(*filter(lambda r:0in r,r))]):
 t=i(i(r));l,={*sum(r,[])}-{0,r[0][0]}
 for i in range(4):
  n=1-2*(i&1);r=[r[::n]for r in r[::-n]];i,z=divmod(sum(r,[]).index(l),len(r[0]));g,u=divmod(sum(r,[]).index(0),len(r[0]))
  c,q=zip(*((i,u)for i,r in enumerate(r)for u,a in enumerate(r)if a<1));a,e=min(c),max(c);c,j=min(q),max(q);n=len(t)-(r[a][c]==r[0][0])    
  if(e<=i)*(j<z):
   a+=i-g;c+=z-u
   while(a<len(r))*(c<len(r[0])):
    for i in range(len(t)):
     for u in range(len(t)):
      if(a+i<len(r))*(c+u<len(r[0])):r[a+i][c+u]=[r[0][0],l][t[i][u]<1]
    a+=n;c+=n
 return r