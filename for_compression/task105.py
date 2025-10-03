def p(g,k=0):
 *g,=map(list,zip(*g))
 X,Y=zip(*((i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v));a,*_,b=sorted(X);c,*_,d=sorted(Y)
 for i,r in enumerate(g):
  for j in range(c,d+1):r[j]=r[j]or 2*(i in[a,b]or r[c+1:d].count(1)>1)
 return g if k else p(g,1)