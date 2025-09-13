def p(g):
 for _ in 0,1:
  for i,r in enumerate(g:=[*map(list,zip(*g))]):
   for j in range(~-len(r)):
    for q in g[i-(i>0):i+2]*(r[j]*r[j+1]==4):q[j-(j>0):j+3]=[x or 3for x in q[j-(j>0):j+3]]
 return g