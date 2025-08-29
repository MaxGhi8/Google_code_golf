def p(g):
 for a,b,c in zip(g,g[1:],g[2:]):
  for j in range(18):
   if sum(a[j:(J:=j+3)]+b[j:J]+c[j:J])<1:a[j:J]=b[j:J]=c[j:J]=[1]*3
 return g