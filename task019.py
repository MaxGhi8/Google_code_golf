def p(g,E=enumerate):
 g=[r*2for r in g*2]
 for i,r in E(g):
  for j,v in E(r):
   if v%8:
    for x,y in[(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]:
     if 0<=x<len(g)and 0<=y<len(r):g[x][y]=g[x][y]or 8
 return g