def p(g):
 m=[r[:]for r in g]
 for I in range(81):
  i,j=I//9,I%9
  if all(s:=sum([r[j:j+2]for r in g[i:i+2]],[])):
   for a in range(len({*s})):m[i+a+2][j:j+2]=[3]*2
 return m