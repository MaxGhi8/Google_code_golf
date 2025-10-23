def p(g):
 c=set();t=[]
 for n in range(100):
  a=n%10;n//=10
  if(n,a)in c:continue
  r=g[n][a];p=[(n,a)];c|={p[0]}
  for f,x in p:
   for a in(f+1,x),(f-1,x),(f,x+1),(f,x-1):
    if-1<a[0]<10>a[1]>-1and a not in c and g[a[0]][a[1]]==r:c|={a};p+=a,
  t+=[(r,{*p})]
 p=[];r,*j=[a for c,a in t if c==5],
 for c,a in t:
  if c<1:
   f=lambda s,p:[min,max][p>1](c[p%2]for c in s)
   if any(all([f(a,c)<=f(n,c),f(a,c)>=f(n,c)][c<2]for c in range(4))for n in r):p+=a,
  elif c-5:j+=[(c,a)]
 r=lambda s:frozenset((a-min(s)[0],n-min(s)[1])for a,n in s);a={};l={}
 for f in p:s=r(f);a[s]=a.get(s,[])+[f]
 for c,f in j:s=r(f);l[s]=l.get(s,[])+[(c,f)]
 k=[c for c,a in j]
 for s,a in a.items():
  if r:=l.get(s):
   if r[1:]:r=[c for c in r if c[0]!=max(k,key=k.count)]or r
  for z,(c,f)in zip(a,r):
   for n,a in f:g[n][a]=0
   for n,a in z:g[n][a]=c
 return g