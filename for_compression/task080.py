def p(p):
 m=len(p);r=p[0];a=min(a+1for a,p in enumerate(r)if p-r[0]);d=[d for o,r in enumerate(p)for r,d in enumerate(r)if{p[max(0,o-a)][r]}-{0,d}and{p[o][max(0,r-a)]}-{0,d}][0];b=[(o,r)for o,r in enumerate(p)for r,p in enumerate(r)if p==d]
 for d in range(9):
  e=d//3-1;u=d%3-1;d=max(p[o+e*a][r+u*a]for o,r in b if m>o+e*a>-1<r+u*a<m)
  for o,r in b:
   if m>o+e*a>-1<r+u*a<m:p[o+e*a][r+u*a]=d
 return p
