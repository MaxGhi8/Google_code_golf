def p(n,d=lambda n:[r for r in zip(*n)if{*r}-{0,5}]):
 u,l=len(z:=d(d(n))),len(z[0])
 for r in range(11-u):
  for a in range(11-l):
   for d in range(u*all(5in r[a:a+l]for r in n[r:r+u])*all(5in d[r:r+u]for d in [*zip(*n)][a:a+l])):n[r+d][a:a+l]=z[d]
 return n