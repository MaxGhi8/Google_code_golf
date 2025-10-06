def p(a):
 i=max(range(1,10),key=sum(a,[]).count);d=({*sum(a,[])}-{0,i}).pop()
 h,*o={(h,s):e for h,s in enumerate(a)for s,e in enumerate(s)if e},
 def c(a):
  if a in h:x,y=a;u.add((x-f,y-l,h.pop(a)));[c((x+d%3-1,y+d//3-1))for d in range(9)]
 for(f,l),q in[*h.items()]:
  if q==d:
   u=set();c((f,l))
   if len(u)>3:
    o+=[u]
    for s,p,u in u:a[s+f][p+l]=0
 c=1,-1;y=lambda s,*h:(h[s&1]*c[s&2>0],h[1^s&1]*c[s&4>0])
 for f,k in enumerate(a):
  for l,q in enumerate(k):
   for e in[*o]*(q==d):
    for h in range(9):
     try:
      if sum(u==a[f+y(h,s,p)[0]][l+y(h,s,p)[1]]!=i for s,p,u in e)>2:
       for s,p,u in e:s,p=y(h,s,p);a[s+f][p+l]=a[s+f][p+l]or i
     except:0
 return a