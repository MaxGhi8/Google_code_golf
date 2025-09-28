def p(f,u=enumerate):
 m=len(f);r=f[0];a=min(a+1for a,f in u(r)if f-r[0]);d=[d for n,r in u(f)for r,d in u(r)if{f[max(0,n-a)][r]}-{0,d}and{f[n][max(0,r-a)]}-{0,d}][0];c=[(n,r)for n,r in u(f)for r,f in u(r)if f==d]
 for t in range(9):
  e=t//3-1;u=t%3-1;d=max(f[n+e*a][r+u*a]for n,r in c if m>n+e*a>-1<r+u*a<m)
  for n,r in c:
   if m>n+e*a>-1<r+u*a<m:f[n+e*a][r+u*a]=d
 return f