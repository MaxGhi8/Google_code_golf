def p(g,E=enumerate):
 for i,r in E(g):
  for j,c in E(r):
   if c==2:
    for x in range(max(0,i-1),min(len(g),i+2)):
     for y in range(max(0,j-1),min(len(r),j+2)):g[x][y]=g[x][y]or 1
 return g