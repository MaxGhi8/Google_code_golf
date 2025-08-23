def p(g,E=enumerate):
 for k in{*sum(g,[])}-{0}:
  (b,a),(d,c)=sorted((j,i)for i,r in E(g)for j,v in E(r)if v==k)
  for x in range(d-b):g[a+[-x,x][a<c]][b+x]=k
 return g