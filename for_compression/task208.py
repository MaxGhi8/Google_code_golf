def p(e):
 g,m=divmod(440-(r:=sum(e,[]))[::-1].index(c:=min(r,key=r.count))-r.index(c),21)
 for r in range(21-g):
  for d in range(21-m):
   if sum(sum(f[d+1:d+m])for f in e[r+1:r+g])<1:
    e[r][d:d-~m]=e[r+g][d:d-~m]=[c]*-~m
    for f in e[r:r-~g]:f[d]=f[d+m]=c
 return e
