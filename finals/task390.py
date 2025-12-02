def p(g):
 for _ in' '*4:
  g=[*zip(*g[::-1])]
  if g[4].count(2)>4:g[1:3],g[6:8]=g[6:8][::-1],g[1:3]
  if g[3].count(2)>4:g[:2],g[5:7]=g[5:7][::-1],g[:2]
 return g