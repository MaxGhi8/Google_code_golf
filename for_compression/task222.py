def p(l):
 for q,r in enumerate(l):
  for u,t in enumerate(r):
    if (sum(r[u-1:u+2].count(t)for r in l[q-1:q+2])>3)*(t in r[u-1:u+2:2])*(t in{r[u]for r in l[q-1:q+2:2]})<1:r[u]=0
 f=max({*(s:=sum(l,[]))}-{0},key=s.count);return[[t*(t==f)for t in r]for r in l]