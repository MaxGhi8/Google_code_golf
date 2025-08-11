def p(g):
 L=range(1,len(g)-1)
 for k in range(999):
  for r in L:
   for c in L:
    if k+g[r][c]<1 and g[r-1][c]*g[r][c-1] and 3 in g[r][c:] and 3 in [x[c]for x in g[r:]]:g[r][c]=4
    if g[r][c]*k==4*k>0 and g[r+1][c]+g[r][c+1]+g[r-1][c]+g[r][c-1]<12:g[r][c]=0
 return g