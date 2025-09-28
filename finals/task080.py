def p(a,E=enumerate):
 d=len(a);r=a[0];j=min(j+1for j,f in E(r)if f-r[0]);g=[g for b,r in E(a)for r,g in E(r)if{a[max(0,b-j)][r]}-{0,g}and{a[b][max(0,r-j)]}-{0,g}][0];o=[(b,r)for b,r in E(a)for r,f in E(r)if f==g]
 for A in range(9):
  e=A//3-1;l=A%3-1;g=max(a[b+e*j][r+l*j]for b,r in o if d>b+e*j>-1<r+l*j<d)
  for b,r in o:
   if d>b+e*j>-1<r+l*j<d:a[b+e*j][r+l*j]=g
 return a