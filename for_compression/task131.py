def p(p):
 for _ in[0]*4:
  u=len(p[0]);n=len(p);b=sum(p,[]);a=b.index(2)//u;f=b.index(3)//u;d=n-b[::-1].index(3)//u
  if u<n and f>a:p=p[:a+1]+p[f:d]+[[8]*u]+[[0]*u]*(n-a+f-d-2)
  *p,=map(list,zip(*p[::-1]))
 return p