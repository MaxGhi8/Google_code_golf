def p(q,E=enumerate):
 d,o,*j={(d,n):e for d,f in E(q)for n,e in E(f)if e},1,
 def B(z):
  if z in d:x,y=z;C.add((x-k[0],y-k[1],d.pop(z)));[B((x+A%3-1,y+A//3-1))for A in range(9)]
 for k,v in[*d.items()]:
  if v==2:j+=[(k,C:=set())];B(k);o=[o,C][any(e&1for*q,e in C)]
 l={s for s in o if s[2]&1};r=o-l;o=1,-1;y=lambda k,*d:(d[k&1]*o[k&2>0],d[1^k&1]*o[k&4>0])
 for(t,p),u in j:
  for k in range(9):
   for*d,e in[*l]*({(*y(k,*d),e)for *d,e in r}==u):f,m=y(k,*d);q[f+t][m+p]=e
 return q