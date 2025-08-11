def p(g):
 k=max(max(g));c=g[-1].index(k);g[0][c+1::4]=[5]*len(g[0][c+1::4]);g[-1][c+3::4]=[5]*len(g[-1][c+3::4])
 for R in g:R[c::2]=[k]*len(R[c::2])
 return g