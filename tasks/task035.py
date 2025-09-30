def p(g):
 for _ in' '*4:
  for r in(g:=[*map(list,zip(*g))][::-1]):
   if r[0]:r[r.index(8)]=r[0]
 return g