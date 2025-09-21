def p(g):
 *m,=map(list,g)
 for i in 0,4*(len(g)>3):
  for j in 0,4,8:
   for a in range(9):m[i+a//3][j+a%3]=g[i+1][j+1]+5
 return m