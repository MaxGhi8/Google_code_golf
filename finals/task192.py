def p(g):
 t=sum(g,[]);k=min({*t}-{0,min(t,key=t.count)})
 for a,b in zip(g,g[1:]):
  for j in range(len(a)-1):
   if min(a[j:j+2]+b[j:j+2]):a[j:j+2]=b[j:j+2]=k,k
 return[[k*(x==k)for x in r]for r in g]