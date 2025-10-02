def p(g):
 h=len(g)-1;R=range(1,h)
 for A in R:
  for c in R:
    if(W:=g[A][c])and(g[A][c+1]==W)^(g[A][c-1]==W)and(g[A+1][c]==W)^(g[A-1][c]==W):
     l,J,p,a=2*(g[A+1][c]==W)-1,2*(g[A][c+1]==W)-1,c,A
     if g[A+l][c+J]-W:
      while h>p>0<a<h:a-=l;p-=J;g[a][p]=g[A+2*l][c+2*J]
 return g