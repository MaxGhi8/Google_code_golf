def p(g):
 n=range(len(g));L=[(i,j)for i in n for j in n if g[i][j]>0]
 for x in range(0,len(L),4):a,b,c,d=L[x]+L[x+3];[g[i].__setitem__(j,2)for i in n for j in n if(a<i<c)*(b<j<d)]
 return g