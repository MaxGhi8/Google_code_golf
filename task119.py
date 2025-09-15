def p(g):
 for _ in ' '*4:
  g=[*map(list,zip(*g))][::-1]
  if 2 not in g[0]:
   i=[i for i in range(12)if any(g[i])][0];c=1
   for j in range(1,12):
    if 8in[*zip(*g)][-1]:j=~j
    if g[i:=i+c][j]==2:c=-1;i+=2*c
    g[i][j]=g[i][j]or 3
 return g