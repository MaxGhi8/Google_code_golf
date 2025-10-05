def p(g,k=0,R=range(15)):
 *g,=map(list,zip(*g))
 if max(r.count(2)for r in g)<5:
  b,*_,d=(j for r in g for j in R if r[j]==2)
  for r in g:
   for j in R:
    if r[j]>2and(d<j or j<b):r[j]=0;r[2*(b,d)[j>=b+d+1>>1]-j]=5
 return k*g or p(g,1)