def p(t,l=range):
 s,i=len(t),len(t[0]);n,o=[],set()
 for u in l(s):
  for d in l(i):
   if a:=t[u][d]:n+=[(u,d,a)];o|={a}
 for(u,d,a)in n:
  r=sorted(o)[a==sorted(o)[0]]
  for y in-1,0,1:
   for a in-1,0,1:
    v,a=u+y,d+a
    if s>v>-1<a<i:t[v][a]=t[v][a]or r
 s,a=n[0][:2];i,n=n[-1][:2]
 if n>a:
  for d in l(a+1,n):
   if min(d-a,n-d)&1<1:t[s][d]=t[i][d]=5
 if i>s:
  for u in l(s+1,i):
   if min(u-s,i-u)&1<1:t[u][a]=t[u][n]=5
 return t