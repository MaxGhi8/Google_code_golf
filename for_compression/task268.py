def p(s,p=lambda s:[*zip(*filter(any,s))]):
 l=d=-1
 for n in'0'*96:
  *s,=map(list,zip(*[[t[n]or(t[:n].count(a:=max(sum(s,[])))==1)*l*(a in t[n:]or t[n-1]==l)for n in range(len(s))]for t in s[::-1]]));d+=(d<0<('0'in str(p(p(s)))))^1;*n,t=filter(any,s)
  if d%4==0<d:
   if(a:=t.index(l)-d//4)>l:t[a]=l
   if(a:=d//4+~t[::-1].index(l))<0:t[a]=l
   d*=l**(s[-1]==t)
 return[[*map({l:4}.get,t,t)]for t in s]
