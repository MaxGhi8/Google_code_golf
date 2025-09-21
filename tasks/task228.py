def p(g,R=range(10)):
 (a,b),*_,(c,d)=[(i+1,j+1)for i in R for j in R if g[i][j]]
 for x,y,X,Y in(a,b,c,d),(a,d-2,c,b-2),(c-2,b,a-2,d),(c-2,d-2,a-2,b-2):g[x][y],g[X][Y]=g[X][Y],g[x][y]
 return g