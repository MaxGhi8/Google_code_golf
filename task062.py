def p(g):
 for _ in' '*4:
  g=[*zip(*g[::-1])]
  for r in range(10):
   for y in[*range(min(9-r,r))]*({*g[r]}=={0,2}and sum(g[r-1])<1):g[r-y]=g[r+y+1]
 return[[c or 3for c in r]for r in g]