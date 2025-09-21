def p(g):
 for i in range(36):
  h=g[a:=i//6][(b:=i%6):b+2]+g[a+1][b:b+2]
  for c in(0,1,2,3)*(sum(h)>16):g[a+c//2][b+c%2]=h[c]or 1
 return g