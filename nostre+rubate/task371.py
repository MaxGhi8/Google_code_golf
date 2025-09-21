def p(g,E=enumerate):
 a,b=map(sum,zip(*((i,j)for i,r in E(g)for j,v in E(r)if v)))
 a//=2;b//=2
 for i in-1,0,1:g[a+i][b]=g[a][b+i]=3
 return g