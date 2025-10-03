def p(a):
 r,k,m=sorted({*(i:=sum(a,[]))},key=i.count)
 for h in'abcd':
  m=0;a=[*map(list,zip(*a))][::-1]
  for i,t in enumerate(a):
   for o,p in enumerate(t):
    if p==k:
     for p in range({4:3,2:0,7:min(3,2+(k<8or'c'!=h)*int(m:=m+.3))}.get(t.count(k),2)):a[i-p][o]=a[i-p][o]or r
 return[[*map({r:k,k:r}.get,t,t)]for t in a]
