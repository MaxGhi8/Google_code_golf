def p(g):
 n=range(len(g));L=[(i,j)for i in n for j in n if g[i][j]>0];return [[[g[i][j],2][any(a<i<c and b<j<d for(a,b),(c,d)in zip(L[::4],L[3::4]))]for j in n]for i in n]