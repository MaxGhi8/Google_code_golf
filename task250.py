def p(g,R=range(10)):
 for _ in'    ':
  for r in(g:=[*map(list,zip(*g[::-1]))])[:(a:=[i for i in R for j in R if g[i][j]==2][0])]:
   for j in R:
    if r[j]:r[j]=0;g[a-1][j]=5
 return g