def p(g,R=range):
 (r,c)=[(i//6,i%6)for i in R(36)if g[i//6][i%6]][0]
 P=[[-2,-2],[2,-2],[-2,2],[2,2]]
 for i in R(4):
   for y,x in P:
    if 6>(a:=r+y+i//2)>-1<(b:=c+x+i%2)<6:g[a][b]=g[r+(y<0)][c+(x<0)]
 return g