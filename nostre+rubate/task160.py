def p(g):
 *m,=map(list,g)
 for i in range(64):
  y=i>>3;x=i&7
  if sum(sum(r[x:x+3])for r in m[y:y+3])>7:
   for a in range(9):g[y+a//3][x+a%3]=2*(186>>a&1)
 return g