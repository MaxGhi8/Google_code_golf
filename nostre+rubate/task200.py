def p(g):
 k=max(r:=g[-1]);c=r.index(k);g[0][c+1::4],r[c+3::4]=[[5]*((k-c)//4)for k in(12,10)]
 for r in g:r[c::2]=[k]*(11-c>>1)
 return g