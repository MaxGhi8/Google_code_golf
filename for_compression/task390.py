def p(l):
 for n in 0,0:
  *l,=map(list,zip(*l))
  if all(5>a.count(2)for a in l):
   z,*n,t=[n for a in l for n in range(15)if a[n]==2];m=z+t+1>>1
   for a in l:
    for n in range(15)[:t]:
     if a[n]>2:a[n]=0;a[(z*2,t*2)[n>=m]-n]=5
 return l