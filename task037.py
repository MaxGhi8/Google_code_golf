def p(g,E=enumerate):
 for k in{*sum(g,[])}-{0}:
  A,B=sorted([(j,i)for i,r in E(g)for j,v in E(r)if v==k]);b,a=A
  for x in range(B[0]-b):g[a+[-x,x][a<B[1]]][b+x]=k
 return g