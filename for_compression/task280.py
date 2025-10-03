def p(g,u=3,e=0):
 for d,r in enumerate(g):
  l=2in r and(e:=r.index(2))<r.index(3)and[*r[e:],0].index(0)
  for r,o in enumerate(r):
   for i in range(l*(r<e)):g[d-i][r]=2+(i>0);g[d+i][r]=2+(i>0)
 return-u*g or p([*map(list,zip(*g[::-1]))],u-1)