def p(g,E=enumerate):
 s,t=sorted(a.index(2)for a in zip(*g)if 2in a);b=[(i,j)for i,r in E(g)for j,v in E(r)if v&8]
 for i in s,t:
  for x,y in b:
   for j,_ in E(q:=g[i+x-s]):q[j]=q[j]or 8*(any(q[:j])&any(q[j:])or i>s);g[x][y]=4
 return g