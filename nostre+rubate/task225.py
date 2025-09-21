def p(g):
 r,c=[(i//6,i%6)for i in range(36)if g[i//6][i%6]][0]
 for i in 0,1,2,3:
  for y in-2,2:
   for x in-2,2:
    if 6>(a:=r+y+(i>1))>-1<(b:=c+x+i%2)<6:g[a][b]=g[r+(y<0)][c+(x<0)]
 return g