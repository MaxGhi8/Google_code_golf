def p(g,f=lambda d:[*filter(any,zip(*d))]):
 x,y=divmod(sum(g,[]).index(5),len(g[0]));g[x][y]=0;m=f(f(g))
 for i in-1,0,1:g[x+i][y-1:y+2]=m[i+1]
 return g