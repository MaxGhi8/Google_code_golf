def p(g,e=enumerate):
 a,b=map(min,zip(*((i,j)for i,r in e(g)for j,v in e(r)if v)))
 for t in range(25):x,y=t//5,t%5;g[a+x][b+y]=max(g[a+x][b+y],g[a+4-y][b+x],g[a+4-x][b+4-y],g[a+y][b+4-x])
 return g