def p(i):
 l,*S={(r,e)for r in range(10)for e in range(10)if i[r][e]},
 def b(z):
  if z in l:l.remove(z);h.add(z);[b((z[0]+r%3-1,z[1]+r//3-1))for r in range(9)]
 while l:S+=[h:=l-l];b(min(l))
 for h in S:
  for a,b in h:i[a][b]=1+(len(h)<max(map(len,S)))
 return i