def p(g,f=lambda g:[r for r in zip(*g)if{*r}-{0,5}],R=range):
 m=len(k:=f(f(g)));n=len(k[0])
 for i in R(11-m):
  for j in R(11-n):
   for a in[*R(m)]*all(5in r[j:j+n]for r in g[i:i+m])*all(5in c[i:i+m]for c in [*zip(*g)][j:j+n]):g[i+a][j:j+n]=k[a]
 return g