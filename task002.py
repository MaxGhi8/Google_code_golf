def p(g,E=enumerate):
 for k in range(999):
  for r,R in E(g[1:-1],1):
   for c,C in E(R[1:-1],1):
    if k+C<1and g[r-1][c]*R[c-1]and 3 in R[c:]and 3 in[x[c]for x in g[r:]]:g[r][c]=4
    if C*k==4*k>0and g[r+1][c]+R[c+1]+g[r-1][c]+R[c-1]<12:g[r][c]=0
 return g