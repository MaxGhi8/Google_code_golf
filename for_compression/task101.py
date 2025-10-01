def p(u,t=[]):
 def p(u):
  if u in e:r[u]=e.pop(u);p((u[0]-1,u[1]));p((u[0]+1,u[1]));p((u[0],u[1]-1));p((u[0],u[1]+1))
 for f in[1]*3:
  e,*o={(p,m):n for p,u in enumerate(u)for m,n in enumerate(u)if n},
  while e:o+=[r:={}];p(min(e));x=0
  for r in o:f,m=min(u for u in r if r[u]>1);1in r.values()and(t or(t:=[(u-f,p-m)for u,p in r if r[u,p]<2]))or(x or(x:=(r,f,m)))
  if x:
   r,f,m=x;i=min(3,int(len(r)**.5))
   for r,n in t:
    for e in range(i*i):u[f+r*i+e//i][max(0,m+n*i+e%i)]=1
 return u