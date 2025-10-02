def p(g,e=enumerate):
 for i,r in e(g):
  for j,v in e(r):
    if (sum(R[j-1:j+2].count(v)for R in g[i-1:i+2])>3)*(v in r[j-1:j+2:2])*(v in{R[j]for R in g[i-1:i+2:2]})<1:r[j]=0
 k=max({*(L:=sum(g,[]))}-{0},key=L.count);return[[v*(v==k)for v in r]for r in g]