def p(q):
 d,*i={(d,n)for d,f in enumerate(q)for n,e in enumerate(f)if e},
 while d:
  n=[d.pop()];l=[]
  while n:
   h,g=n.pop();l+=[(h,g,e:=q[h][g])]
   if e==2:f=h,g
   for e in range(9):
    if(e:=(h+e//3-1,g+e%3-1))in d:d.remove(e);n+=e,
  t,p=f;e={(d-t,n-p,e)for d,n,e in l}
  if any(e&1for*q,e in l):o=e
  i+=(f,e),
 l={h for h in o if h[2]&1};r=o-l;o=1,-1;y=lambda g,d,n:([d,n][g&1]*o[g&2>0],[n,d][g&1]*o[g&4>0])
 for(t,p),z in i:
  for g in range(8):
   if{(*y(g,d,n),e)for d,n,e in r}==z:
    for d,n,e in l:
     f,m=y(g,d,n);q[f+t][m+p]=e
 return q