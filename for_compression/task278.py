def p(l):
 for i in 0,1:
  for i,r in enumerate(l:=[*map(list,zip(*l))]):
   for t in range(~-len(r)):
    for s in l[i-(i>0):i+2]*(r[t]*r[t+1]==4):s[t-(t>0):t+3]=[i or 3for i in s[t-(t>0):t+3]]
 return l