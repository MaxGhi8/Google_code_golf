def p(n):
 s,i={*sum(n,[])}-{0}
 if[i,i]!=sum(n,[])[sum(n,[]).index(i)+19:][:2]:s,i=i,s
 for r in range(400):
  for r in(n[e:=r//20][d:=r%20]==i)*[*range(e,20)]*(s in[*zip(*n[e:])][d]):n[r][d]=n[r][d]or s
 return n