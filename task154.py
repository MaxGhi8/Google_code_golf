def p(g,R=range(15)):
 for _ in'  ':
   g=[*map(list,zip(*g))]
   if max(r.count(2)for r in g)<5:
    b,*_,d=[j for r in g for j in R if r[j]==2];m=-~(b+d)//2
    for r in g:
     for j in R:
      if r[j]>2and(d<j or j<b):r[j]=0;r[(2*b,2*d)[j>=m]-j]=5
 return g