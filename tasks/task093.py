def p(g,c=enumerate):
 for i,f in{(i,f)for i,r in c(g)for f,j in c(r)if j==5}:
  for a,r in(0,1),(0,-1),(1,0),(-1,0):
   d=j=i+a;y=y=f+r
   while-1<j<14 and-1<y<14 and g[j][y]-5:
    if g[j][y]%5:g[d][y]=5;g[j][y]*=j^d|y^y<1;d+=a;y+=r
    j+=a;y+=r
 return g