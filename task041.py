def p(g,A=0):
 for r in g:
  for j,k in enumerate(r):
   if k:A=(not A)*k
   else:r[j]=A
 return g