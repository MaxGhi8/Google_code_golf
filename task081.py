def p(g):
 for I in range(36):
  for c,x in enumerate(H:=g[i:=I//6][(j:=I%6):j+2]+g[i+1][j:j+2]):
   if sum(H)>16:g[i+c//2][j+c%2]=x or 1
 return g