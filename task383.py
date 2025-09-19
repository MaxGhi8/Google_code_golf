def p(g,e=enumerate):
 for _ in' '*4:
  *g,=map(list,zip(*g[::-1]))
  b,k=min((j,v)for i,r in e(g[:-1])for j,v in e(r)if v*g[i-1][j]*g[i+1][j])
  for r in g:
   for j,v in e(r*(0<r[b+1]!=k)):r[j]=[({*sum(g,[])}-{0,k}).pop(),k][v>0]
 return g