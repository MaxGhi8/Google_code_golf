def p(g,E=enumerate):
 for i,r in E(g):
  for j,_ in E(r[:-1]):
   if(A:=r[j-1])*(B:=r[j+1])and A==B==g[i-1][j]:g[-1][j]=4
 return g