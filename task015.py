def p(g):
 for t in range(576):r,c,I=t//72,t//9%8,t%9;i,j=I//3-1,t%3-1;g[r+i][c+j]=I%2*7*((v:=g[r][c])==1)or g[r+i][c+j]or(I%2<1)*4*(v==2)
 return g