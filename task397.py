def p(g):
 m=[*map(list,g)]
 for I in range(81):
  i,j=I//9,I%9
  if all(s:=g[i][j:j+2]+g[i+1][j:j+2]):
   for a in range(len({*s})):m[i+a+2][j:j+2]=3,3
 return m