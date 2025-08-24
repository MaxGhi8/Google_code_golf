def p(g,A=0):
 for r in g:
  for j,k in enumerate(r):r[j]=k|A;A=(A<1)*k+(k<1)*A
 return g