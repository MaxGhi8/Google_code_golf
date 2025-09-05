def p(g):
 for i,r in enumerate(g):r[i]=g[~i][i]=0
 return g