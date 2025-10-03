def p(o):
 for n in' '*4:
  *o,=map(list,zip(*o[::-1]))
  n,i=min((z,p)for i,r in enumerate(o[:-1])for z,p in enumerate(r)if p*o[i-1][z]*o[i+1][z])
  for r in o:
   for z,p in enumerate(r*(0<r[n+1]!=i)):r[z]=[({*sum(o,[])}-{0,i}).pop(),i][p>0]
 return o