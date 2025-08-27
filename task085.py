def p(g,E=enumerate):
 for i,r in E(g[1:]):
  for j,v in E(r[1:],1):r[j]=any([p[j-1:j+2]!=3*[v]for p in g[i:i+3]])*v
 return g