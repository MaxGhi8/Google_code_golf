def p(g,f=lambda g:[[*r]for r in zip(*g)if{*r}-{0,8}],R=range):
 m=len(k:=f(f(g)));n=len(k[0]);o=[[0]*10for _ in' '*10]
 for i in R(11-m):
  for j in R(11-n):
   for a in[*R(m*n)]*all(8in r[j:j+n]for r in g[i:i+m])*all(8in c[i:i+m]for c in [*zip(*g)][j:j+n]):o[i+a//n][j+a%n]=k[a//n][a%n]
 return o