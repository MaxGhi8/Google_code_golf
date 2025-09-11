def p(g):
 for _ in 0,1:
  for i,r in enumerate(g:=[*map(list,zip(*g))]):
   for j in range(len(r)-1):
    for q in g[i and i-1:i+2]*(r[j]*r[j+1]==4):q[j and j-1:j+3]=[x or 3for x in q[j and j-1:j+3]]
 return g