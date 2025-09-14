def p(g,R=range):
 r=len(g);c=len(g[0]);b=0
 for h in R(1,r):
  for v in R(1,c):
   q=[[0]*10 for _ in R(4)]
   for i in R(r):
    for j in R(c):q[(i<h)*2+(j<v)][g[i][j]]+=1
   s=f=-1
   for t in q:
    m=max(t);s+=m;u=sum(t)-m
    if u>f:f,y=u,t.index(m)
   if s>b:b,x=s,y
 return[[x]]