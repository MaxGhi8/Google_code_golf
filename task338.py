def p(g,E=enumerate):
 for r,R in E(g[1:-1],1):
  for c,C in E(R[1:-1],1):g[r][c]=[C,3][(C<1)*g[r-1][c]*R[c-1]>0]
 return[[c*(c!=2)for c in r]for r in g]
