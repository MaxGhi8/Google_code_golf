def p(m):
 j,f=sorted(e.index(2)for e in zip(*m)if 2in e);z=[(i,d)for i,d in enumerate(m)for d,v in enumerate(d)if v&8]
 for i in 0,f-j:
  for a,e in z:
   for d,w in enumerate(q:=m[i+a]):q[d]=w or(any(q[:d])&any(q[d:])or i>0)*8;m[a][e]=4
 return m
