def p(g):
 A={}
 for r in g:
  for c,k in enumerate(r):
   if k>4:r[c]=A.setdefault(c,len(A)+1)
 return g