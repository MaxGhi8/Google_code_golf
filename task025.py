def p(g,E=enumerate,f=lambda x:[*zip(*x)]):
 g=(f(g),g)[t:=1-any(a&b for a,b,*_ in g)];z=[[0]*-~-~len(f(g))for _ in g]
 for i,r in E(f(g)):
  for j,v in[*E(r)]*all(r):z[j][i:i+3]=v*(v in g[j][:i]),v,v*(v in g[j][i+1:])
 return[z:=f(z)[1:-1],f(z)][t]
