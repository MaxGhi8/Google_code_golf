def p(u,n=[]):
 def p(u):
  if u in e:r[u]=e.pop(u);p((u[0]-1,u[1]));p((u[0]+1,u[1]));p((u[0],u[1]-1));p((u[0],u[1]+1))
 for f in[1]*3:
  e,*o={(p,m):n for p,u in enumerate(u)for m,n in enumerate(u)if n},
  while e:o+=[r:={}];p(min(e));x=0
  for r in o:f,m=min(u for u in r if r[u]>1);1in r.values()and(n or(n:=[(u-f,p-m)for u,p in r if r[u,p]<2]))or(x or(x:=(r,f,m)))
  if x:
   r,f,m=x;t=min(3,int(len(r)**.5))
   for r,x in n:
    for e in range(t*t):u[f+r*t+e//t][max(0,m+x*t+e%t)]=1
 return u