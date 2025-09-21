def p(g,f=lambda a,b,c:a*(a>1)or b**(b==c)):
 for i,r in enumerate(g):
  r[3:5]=map(f,r[3:5],r[:2],r[6:])
  if 2<i<5:r[:]=map(f,r,g[i-3],g[i+3])
 return g