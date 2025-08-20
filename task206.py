def p(g,f=lambda d:[[*r]for r in zip(*d)if(5not in r or sum(r)>5)*any(r)]):
 x,y=divmod(sum(g,[]).index(5),len(g[0]));m=f(f(g))
 for i in(-1,0,1):
  g[x+i][y-1:y+2]=m[i+1][:]
 return g