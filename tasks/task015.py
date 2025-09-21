def p(g):
 for I in range(576):r,c,j=I//72,I//9%8,I%3-1;I%=9;i=I//3-1;g[r+i][c+j]=I%2*7*((v:=g[r][c])==1)or g[r+i][c+j]or(I%2<1)*4*(v==2)
 return g