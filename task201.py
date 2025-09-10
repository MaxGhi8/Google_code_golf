def p(g,e=enumerate,f=lambda d:[*filter(any,zip(*d))]):
 (a,b),*_,(c,d)=[(i,j)for i,r in e(g)for j,v in e(r)if v==4];G=g[a:-~c];m=[r[b:-~d]for r in G]
 for r in G:r[b:-~d]=[0]*-~(d-b);C=f(f(g))
 for i,r in e(C):m[i+1][1:-1]=r[::1-2*(m[1][0]not in next(zip(*C)))]
 return m