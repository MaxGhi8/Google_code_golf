def p(g):
 k=max(g[-1]);c=g[-1].index(k);g[0][c+1::4],g[-1][c+3::4]=([5]*((k-c)//4)for k in[12,10])
 for R in g:R[c::2]=[k]*((11-c)//2)
 return g