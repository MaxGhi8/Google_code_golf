def p(g):
 r,c=divmod(sum(g,[]).index(4),11);m=[[5*(v==5)for v in r]for r in g]
 for I in range(9):m[r*4&12|I//3][c*4&12|I%3]=g[r&-4|I//3][c&-4|I%3]
 return m