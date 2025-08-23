def p(g,k=0):
 g=[*map(list,zip(*g))];n=len(g[0]);(c,b,a),(f,e,d),*_=sorted((i%n,i//n,v)for i,v in enumerate(sum(g,[]))if v)
 if b*e in{0,(len(g)-1)**2}:
  for r in g:
   for j in range(c,n,f-c):r[j]=[a,d][(j-c)//(f-c)%2]
 return g if k else p(g,1)