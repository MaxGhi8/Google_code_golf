def p(g,E=enumerate):
 for k in{*sum(g,[])}:
  X,Y=zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v==k]);m=[r[min(Y):max(Y)+1]for r in g[min(X):max(X)+1]]
  if m==[r[::-1]for r in m]:return m