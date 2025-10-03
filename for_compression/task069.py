def p(g,f=lambda g:[r for*r,in zip(*g)if{*r}-{0,8}]):
 m=len(j:=f(f(g)));n=len(j[0]);f=[[0]*10for e in' '*10]
 for b in range(11-m):
  for e in range(11-n):
   for a in[*range(m*n)]*all(8in r[e:e+n]for r in g[b:b+m])*all(8in r[b:b+m]for r in [*zip(*g)][e:e+n]):f[b+a//n][e+a%n]=j[a//n][a%n]
 return f
