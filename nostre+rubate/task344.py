def p(g,e=enumerate):
 for i,r in e(g):
  for j,v in e(r):
   for x,y in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
    try:
     if 3==v==g[x][y]+1and-1<x|y:r[j]=8;g[x][y]=0
    except:0
 return g