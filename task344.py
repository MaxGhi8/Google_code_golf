def p(g,e=enumerate):
 for i,r in e(g):
  for j,v in e(r):
   for x,y in(i+1,j),(i-1,j),(i,j+1),(i,j-1):
    try:
     if v==3and g[x][y]==2and(x|y)>=0:r[j]=8;g[x][y]=0
    except:0
 return g