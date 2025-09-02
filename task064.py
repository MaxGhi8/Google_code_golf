def p(g):
 s=sum(g,[]);a,b,*_=sorted({*s},key=lambda x:(s.count(x),x))
 for _ in' '*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
   try:i=r.index(a);j=r.index(b);r[i:j]=[a]*(j-i)
   except:0
 return g