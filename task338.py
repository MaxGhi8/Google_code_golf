def p(g,E=enumerate):
 for r,R in E(g[1:-1],1):
  for c,C in E(R[1:-1],1):
   if C<1and g[r-1][c]*R[c-1]and 2in R[c:]and 2in[*zip(*g)][c][r:]:g[r][c]=3
 return[[c*(c!=2) for c in r]for r in g]
