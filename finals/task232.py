def p(g):
 for r in g:
  for j,v in enumerate(r):r[j]=v or(0<r[j-1]!=5)*5or r[j-2]
 return g