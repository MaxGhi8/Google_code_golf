def p(i):
 r=len(i);n=len(i[0]);b=0
 for m in range(1,r):
  for s in range(1,n):
   g=[[0]*10for t in range(4)]
   for t in range(r):
    for e in range(n):g[(t<m)*2+(e<s)][i[t][e]]+=1
   s=f=-1
   for t in g:
    e=max(t);u=sum(t)-e;s+=e
    if u>f:f,y=u,t.index(e)
   if s>b:b,o=s,y
 return[[o]]