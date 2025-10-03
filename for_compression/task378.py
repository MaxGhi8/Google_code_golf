def p(g):
 m=len(g)-1;R=range(1,m)
 for f in R:
  for c in R:
    if(W:=g[f][c])and(g[f][c+1]==W)^(g[f][c-1]==W)and(g[f+1][c]==W)^(g[f-1][c]==W):
     l,z,p,a=2*(g[f+1][c]==W)-1,2*(g[f][c+1]==W)-1,c,f
     if g[f+l][c+z]-W:
      while m>p>0<a<m:a-=l;p-=z;g[a][p]=g[f+2*l][c+2*z]
 return g