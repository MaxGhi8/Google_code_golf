def p(g):
 n=range(len(g));L=[(i,j)for i in n for j in n if g[i][j]>0]
 for x in range(0,len(L),4):a,b,c,d=L[x]+L[x+3];g=[[[g[i][j],2][(a<i<c)*(b<j<d)]for j in n]for i in n]
 return g