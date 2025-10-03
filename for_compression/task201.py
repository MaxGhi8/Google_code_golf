def p(q,f=lambda a:[*filter(any,zip(*a))]):
 (z,b),*_,(c,a)=[(i,j)for i,r in enumerate(q)for j,k in enumerate(r)if k==4];n=q[z:-~c];p=[r[b:-~a]for r in n]
 for r in n:r[b:-~a]=[0]*-~(a-b)
 for i,r in enumerate(f:=f(f(q))):p[-~i][1:-1]=r[::2*(p[1][0]in[*zip(*f)][0])-1]
 return p