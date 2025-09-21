def p(g,E=enumerate):
 for k in range(9):
  for r,R in E(g[1:-1],1):
   for c,C in E(R[1:-1],1):
    if k+C<1and g[r-1][c]*R[c-1]and 3in R[c:]and 3in[*zip(*g)][c][r:]:g[r][c]=4
    if 0<k==C*k/4and g[r+1][c]+R[c+1]+g[r-1][c]+R[c-1]<12:g[r][c]=0
 return g