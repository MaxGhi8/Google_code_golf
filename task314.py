def p(g,f=lambda a,b,c:a*(a>1)or b**(b==c)):
 for i,r in enumerate(g):
  for j in 3,4:r[j]=f(r[j],r[j-3],r[j+3])
  if 2<i<5:
   for j in range(8):r[j]=f(r[j],g[i-3][j],g[i+3][j])
 return g