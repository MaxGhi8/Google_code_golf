def p(g,h=2,L=[[0,4,0],[12,18,9]]):
 for r in g:
  k=0;h+=r[0]>7
  for j,v in enumerate(r):
   if v>7:k+=1
   else:r[j]=L[h%2][k]//h
 return g