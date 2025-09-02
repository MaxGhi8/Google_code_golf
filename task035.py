def p(g,e=enumerate):
 (a,b),*_,(c,d)=[(i,j)for i,r in e(g)for j,v in e(r)if v==8]
 for r in g[a:c+1]:r[b],r[d]=r[0]or r[b],r[9]or r[d]
 while d>=b:g[a][d],r[d]=g[0][d]or g[a][d],g[9][d]or r[d];d-=1
 return g