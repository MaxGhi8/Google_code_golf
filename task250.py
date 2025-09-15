def p(g):
 for _ in" "*4:
  a=sum(g:=[*map(list,zip(*g[::-1]))],[]).index(2)//10
  for r in g[:a]:
   for j in range(10):
    if r[j]:r[j]=0;g[a-1][j]=5
 return g