def p(g):
 for _ in' '*4:
  g=[*map(list,zip(*g[::-1]))];s=sum(g,[])+[2];k=({*s}-{0,2}).pop();a,b=divmod(s.index(2),9)
  while 9>a>-1<b<9and g[a+1][b]*g[a+1][b+1]:g[a][b]=k;g[a and a-1][b]=k;g[a][b and b-1]=k;a-=1;b-=1
 return g