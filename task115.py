def p(g):
 A=[]
 for r in g:
  for v in r:A+=[v]*(v not in A)
 return [[A],[[x]for x in A]][A[0]==g[0][-1]]