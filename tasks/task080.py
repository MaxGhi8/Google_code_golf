def p(g,E=enumerate):
 H=len(g);r=g[0];j,v=min((j+1,v)for j,v in E(r)if v-r[0])
 *A,=dict.fromkeys(k for x,r in E(g)for y,k in E(r)if({g[max(0,x-j)][y]}-{0,k})and({g[x][max(0,y-j)]}-{0,k}));k=A[0];L=[(x,y)for x,r in E(g)for y,v in E(r)if v==k]
 for A in range(9):
  a=A//3-1;b=A%3-1;s=max(g[x+a*j][y+b*j]for x,y in L if H>x+a*j>-1<y+b*j<H)
  for x,y in L:
   if H>x+a*j>-1<y+b*j<H:g[x+a*j][y+b*j]=s
 return g