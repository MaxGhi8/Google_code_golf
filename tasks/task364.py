def p(g,E=enumerate):
 P={(r,c)for r,R in E(g)for c,v in E(R)if v}
 def B(z):
  if z in P:P.remove(z);C.add(z);[B((z[0]+A%3-1,z[1]+A//3-1))for A in range(9)]
 while P:
  C=P-P;B(min(P))
  for a,b in C:g[a][b]=(0,1,6,2)[sum(len({(r,c),(r+1,c),(r,c+1),(r+1,c+1)}&{*C})==3for r,R in E(g)for c,v in E(R))]
 return g