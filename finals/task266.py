def p(g):
 i,j=divmod(sum(g,[]).index(2),5);g[i][j]=0
 for y,x,v in(-1,-1,3),(-1,1,6),(1,-1,8),(1,1,7):
  if 3>i+y>-1<j+x<5:g[i+y][j+x]=v
 return g