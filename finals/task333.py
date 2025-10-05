def p(g,k=2):
 for r in(g:=[*map(list,zip(*g[::-1]))]):
  if 3 in r:I=r.index;j=I(3);i=I(a:=max(r[:j]));r[i:j]=[a]*(j-i)
 return-k*g or p(g,k-1)