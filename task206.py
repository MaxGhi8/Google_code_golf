def p(g):
 x,y=divmod(sum(g,[]).index(5),len(g[0]));g[x][y]=0;q=zip(*filter(any,zip(*filter(any,g))))
 for i in-1,0,1:g[x+i][y-1:y+2]=next(q)
 return g