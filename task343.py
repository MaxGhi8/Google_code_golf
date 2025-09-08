def p(g):
 for r in g:
  n=15;p=1
  while n and r[n-1]<1:n-=1
  for p in range(1,n+1):
   if r[:n-p]==r[p:n]:break
  while n<15:r[n]=r[n-p];n+=1
 return g