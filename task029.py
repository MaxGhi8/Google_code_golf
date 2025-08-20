def p(g,E=enumerate):
 for k in{*(x:=sum(g,[]))}:
  (a,b),*_,(c,d)=[(i,j)for i,r in E(g)for j,v in E(r)if v==k]
  if x.count(k)==2*(c-a+d-b)and g[c].count(k)==d-b+1:break
 return[r[b+1:d]for r in g[a+1:c]]