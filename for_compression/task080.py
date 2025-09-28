def p(a):
 d=len(a);r=a[0];j=min(j+1for j,f in enumerate(r)if f-r[0]);g=[g for b,r in enumerate(a)for r,g in enumerate(r)if{a[max(0,b-j)][r]}-{0,g}and{a[b][max(0,r-j)]}-{0,g}][0];o=[(b,r)for b,r in enumerate(a)for r,f in enumerate(r)if f==g]
 for e in-1,0,1:
  for l in-1,0,1:
   g=max(a[b+e*j][r+l*j]for b,r in o if d>b+e*j>-1<r+l*j<d)
   for b,r in o:
    if d>b+e*j>-1<r+l*j<d:a[b+e*j][r+l*j]=g
 return a