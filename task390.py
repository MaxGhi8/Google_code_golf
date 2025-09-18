def p(g,R=range(15)):
 for _ in 0,0:
  g=[*map(list,zip(*g))]
  if all(5>r.count(2)for r in g):
   b,*_,d=[j for r in g for j in R if r[j]==2];m=b+d+1>>1
   for r in g:
    for j in R[:d]:
     if r[j]>2:r[j]=0;r[(b*2,d*2)[j>=m]-j]=5
 return g