def p(b):
 i=sum(b,[]);i=min({*i}-{0,min(i,key=i.count)})
 for n,r in zip(b,b[1:]):
  for q in range(len(n)-1):
   if min(n[q:q+2]+r[q:q+2]):n[q:q+2]=r[q:q+2]=i,i
 return[[i*(q==i)for q in q]for q in b]
