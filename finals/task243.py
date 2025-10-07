def p(g,E=enumerate):
 for i,r in E(g):
  for j,a in E(r):
   if a<1and 1in(g[i-(i>0)][j],r[j-(j>0)],g[i+(i+1<len(g))][j],r[j+(j+1<len(r))]):r[j]=1;return p(g)
 return g