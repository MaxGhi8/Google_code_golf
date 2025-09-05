def p(g,E=enumerate):
 for k in range(9):
  for r,R in E(g[1:-1],1):
   for c,C in E(R[1:-1],1):g[r][c]|=k+C<1and g[r-1][c]*R[c-1]and 2in R[c:]and 2in[*zip(*g)][c][r:]
 return g