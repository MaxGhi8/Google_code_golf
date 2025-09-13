def p(g,R=range,N=2):
 for f,a,b,c,d in sorted((-all(sum((r[b:b+h]for r in g[a:a+k]),[]))*k*h,a,b,a+k,b+h)for a in R(9)for b in R(9)for k in R(11-a)for h in R(11-b)):
  for i in R(a+1,c-1):
   for j in[*R(b+1,d-1)]*-f:g[i][j]-=(g[i][j]>2)*N
  N=3
 return g