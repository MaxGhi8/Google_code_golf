def p(g,E=enumerate):
 D={};n=len(g[0])
 for i,r in E(g[::-1]):
  for j,v in E(r[::-1]):
   if D.setdefault(v,(i,j))*v*(i-D[v][0])*(j-D[v][1]):r[n+~j]=0;r[n-j]=v
 return g