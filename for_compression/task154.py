def p(o,a=0):
 *o,=map(list,zip(*o))
 if max(r.count(2)for r in o)<5:
  e,*r,u=(i for r in o for i in range(15)if r[i]==2)
  for r in o:
   for i in range(15):
    if r[i]>2and(u<i or i<e):r[i]=0;r[2*(e,u)[i>=e+u+1>>1]-i]=5
 return a*o or p(o,1)