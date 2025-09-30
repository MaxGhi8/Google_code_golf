def p(g,k=3,I=0,E=enumerate):
 for i,r in E(g):
  C=2in r and(I:=r.index(2))<r.index(3)and[*r[I:],0].index(0)
  for j,_ in E(r):
   for c in range(C*(j<I)):g[i-c][j]=2+(c>0);g[i+c][j]=2+(c>0)
 return-k*g or p([*map(list,zip(*g[::-1]))],k-1)