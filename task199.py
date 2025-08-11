def p(g,E=enumerate):
 k,r,c=max((v,i,j)for i,r in E(g)for j,v in E(r));g[r+1][c]=k
 for R in g[:r+1]:R[c%2::2]=[4]*len(R[c%2::2])
 return g