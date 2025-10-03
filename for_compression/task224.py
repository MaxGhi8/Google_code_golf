def p(g):
 n=({*sum(g,[])}-{0,5}).pop();a=c=9;f=d=0
 for o in range(len(g)):
  for e in range(len(g[0])):
   if g[o][e]==5:a=min(a,o);f=max(f,o);c=min(c,e);d=max(d,e)
 for o in range(a+1,f):
  for e in range(c+1,d):g[o][e]=n*(o in{a+1,f-1}or e in{c+1,d-1})or g[o][e]
 return g