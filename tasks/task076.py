def p(q,E=enumerate):
 d,*j={(d,n)for d,f in E(q)for n,e in E(f)if e},
 while d:
  g=[d.pop()];l=[]
  while g:
   s,k=g.pop();l+=[(s,k,e:=q[s][k])]
   if e==2:f=s,k
   for e in range(9):
    if(e:=(s+e//3-1,k+e%3-1))in d:d.remove(e);g+=e,
  t,p=f;e={(d-t,n-p,e)for d,n,e in l}
  if any(e&1for*q,e in l):o=e
  j+=(f,e),
 l={s for s in o if s[2]&1};r=o-l;o=1,-1;y=lambda k,d,n:([d,n][k&1]*o[k&2>0],[n,d][k&1]*o[k&4>0])
 for(t,p),u in j:
  for k in range(8):
   if{(*y(k,d,n),e)for d,n,e in r}==u:
    for d,n,e in l:
     f,m=y(k,d,n);q[f+t][m+p]=e
 return q