def p(G,E=range(10)):
 P,*S={(r,c)for r in E for c in E if G[r][c]},
 def B(z):
  if z in P:P.remove(z);C.add(z);[B((z[0]+A%3-1,z[1]+A//3-1))for A in range(9)]
 while P:S+=[C:=P-P];B(min(P))
 for C in S:
  for a,b in C:G[a][b]=1+(len(C)<max(map(len,S)))
 return G