def p(g,E=enumerate):
 for k in{*sum(g,[])}-{0}:
  X,Y=zip(*((i,j)for i,r in E(g)for j,v in E(r)if v==k));a=min(Y);b=max(Y)+1
  for r in g[min(X):max(X)+1]:r[a:b]=[k]*(b-a)
 return g