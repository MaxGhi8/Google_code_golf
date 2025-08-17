def p(g,k=0):
 for r in(g:=[[*c]for c in zip(*g)]):
  if{*r[1:-1]}<={0,3}:r[1:-1]=[3]*(len(g)-2)
 return g if k else p(g,1)