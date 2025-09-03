def p(g,E=enumerate):
 for r,R in E(g[1:-1],1):
  for c,C in E(R[1:-1],1):R[c]=C or g[r-1][c]>0<R[c-1]and+3
 return[[c*(c!=2)for c in r]for r in g]