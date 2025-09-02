def p(g,e=enumerate):
 (a,b),*_,(c,d)=[(i,j)for i,r in e(g)for j,v in e(r)if v==8]
 for r in g[a:c+1]:r[b]=r[0]or r[b];r[d]=r[9]or r[d]
 for j in range(b,d+1):g[a][j]=g[0][j]or g[a][j];r[j]=g[9][j]or r[j]
 return g