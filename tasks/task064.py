def p(g):
 *_,a,b,_=sorted(range(10),key=sum(g,[]).count)
 for _ in' '*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   if{a,b}<{*r}:I=r.index;i,j=I(a),I(b);r[i:j]=[a]*(j-i)
 return g