def p(g,R=range,N=0):
 for f,a,b,c,d in sorted((-all(all(r[b:b+h])for r in g[a:a+k])*k*h,a,b,a+k,b+h)for a in R(9)for b in R(9)for k in R(11-a)for h in R(11-b)):
  for i in R(a+1,c-1):
   for j in[*R(b+1,d-1)]*-f:g[i][j]=2-(g[i][j]!=2)*N
  N=1
 return g