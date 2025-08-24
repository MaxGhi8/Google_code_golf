def p(g,h=2):
 for r in g:
  k=0;h+=r[0]>7
  for j,v in enumerate(r):
   if v>7:k+=1
   else:r[j]=((0,4,0),(12,18,9))[h&1][k]//h
 return g