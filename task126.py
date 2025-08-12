def p(g):
 for i in range(len(g)):
  for j in range(len(g[0])-1):
   if(A:=g[i][j-1])*(B:=g[i][j+1])and A==B==g[i-1][j]:g[-1][j]=4
 return g