def p(l):
 for r in'  ':
  *l,=map(list,zip(*l))
  if max(r.count(2)for r in l)<5:
   q,*r,u=(s for r in l for s in range(15)if r[s]==2)
   for r in l:
    for s in range(15):
     if r[s]>2and(u<s or s<q):r[s]=0;r[2*(q,u)[s>=q+u+1>>1]-s]=5
 return l
