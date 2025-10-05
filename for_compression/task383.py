def p(f,r=2):
 *f,=map(list,zip(*f[::-1]))
 u,i=min((t,s)for i,e in enumerate(f[:-1])for t,s in enumerate(e)if s*f[i-1][t]*f[i+1][t])
 for e in f:
  for t,s in enumerate(e*(0<e[u+1]!=i)):e[t]=[({*sum(f,[])}-{0,i}).pop(),i][s>0]
 return-r*f or p(f,r-1)