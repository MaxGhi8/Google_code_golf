def p(g,E=enumerate):
 for r,R in E(g[1:],1):
  for c,C in E(R[1:],1):R[c]|=C<1and g[r-1][c]*R[c-1]and 2in{*R[c:]}&{*[*zip(*g)][c][r:]}
 return g