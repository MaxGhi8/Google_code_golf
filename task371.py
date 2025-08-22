def p(g,E=enumerate):
 X,Y=zip(*((i,j)for i,r in E(g)for j,v in E(r)if v))
 for x,y in zip([0,-1,1,0,0],[0,0,0,-1,1]):g[sum(X)//2+x][sum(Y)//2+y]=3
 return g