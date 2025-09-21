def p(g,k=4):
 for r in g:
  for j,v in enumerate(r):
   if 1>r[j-1]<len({*r[j-1:j+2]})>2:r[j:]=[k or v for k in r[j:]]
 return k and p([*map(list,zip(*g[::-1]))],k-1)or g