def p(g):
 for s in 5,4,3:
   for I in range(169):
    i=I//13;j=I%13
    if sum([r[j:j+s]for r in g[i:i+s]],[]).count(5)==~-s*4:
      for r in g[i+1:i+s-1]:r[j+1:j+s-1]=[s+3]*(s-2)
 return g