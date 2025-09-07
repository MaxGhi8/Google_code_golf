def p(g):
 for i,r in enumerate(g):
  if 2in r:j=r.index(2);r[j]=0;break
 for y,x,v in(-1,-1,3),(-1,1,6),(1,-1,8),(1,1,7):
  if 3>i+y>-1<j+x<5:g[i+y][j+x]=v
 return g
