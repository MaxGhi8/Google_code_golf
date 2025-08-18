def p(g,C=range(5)):
 for i in 0,6,12:
  for j in 0,6,12:
   for x in C:
    for y in C:g[i+x][j+y]|=g[x][y]&~g[i+x][j+y]and g[5][0]
 return g
