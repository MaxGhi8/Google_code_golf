def p(g):
 for _ in' '*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
    try:I=r.index;j=I(3);i=I(a:=max(r[:j]));r[i:j]=[a]*(j-i)
    except:0
 return g