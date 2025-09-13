def p(g,R=range,N=0):
 for f,a,b,k,h in sorted((-all(all(r[b:b+h])for r in g[a:a+k])*k*h,a,b,k,h)for a in R(9)for b in R(9)for k in R(11-a)for h in R(11-b)):
  for r in g[a+1:a+~-k]*-f:
   for j in R(b+1,b+~-h):r[j]=2-(r[j]!=2)*N
  N=1
 return g