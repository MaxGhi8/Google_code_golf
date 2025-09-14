def p(g,R=range):
 m,n=len(g),len(g[0])
 for a,b,c,d in[(a,b,a+k,b+h)for a in R(m)for b in R(n)for k in R(3,-~m-a)for h in R(3,-~n-b)if all(g[a][b:b+h]+g[a+k-1][b:b+h]+[r[i]for r in g[a:a+k]for i in(b,b+h-1)])]:
  for i in R(a,c):
   for j in R(b,d):g[i][j]=3*(i in{a,c-1}or j in{b,d-1})
 return g