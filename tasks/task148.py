def p(g,E=enumerate):
 s,t=sorted(a.index(2)for a in zip(*g)if 2in a);b=[(i,j)for i,r in E(g)for j,v in E(r)if v&8]
 for i in 0,t-s:
  for x,y in b:
   for j,w in E(q:=g[i+x]):q[j]=w or(any(q[:j])&any(q[j:])or i>0)*8;g[x][y]=4
 return g