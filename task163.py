def p(g):
 r,c=divmod(sum(g,[]).index(4),11);m=[[5*(v==5)for v in r]for r in g]
 for I in range(9):i,j=I//3,I%3;m[r%4*4+i][c%4*4+j]=g[r//4*4+i][c//4*4+j]
 return m