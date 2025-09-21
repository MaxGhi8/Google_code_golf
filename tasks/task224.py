def p(g,R=range):
 C=({*sum(g,[])}-{0,5}).pop();a=c=9;b=d=0
 for r in R(len(g)):
  for e in R(len(g[0])):
   if g[r][e]==5:a=min(a,r);b=max(b,r);c=min(c,e);d=max(d,e)
 for r in R(a+1,b):
  for e in R(c+1,d):g[r][e]=C*(r in{a+1,b-1}or e in{c+1,d-1})or g[r][e]
 return g