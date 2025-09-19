def p(g):
 for _ in' '*4:
  *g,=map(list,zip(*g[::-1]));c=0
  if 2 not in g[0]+g[-1]+[r[-1]for r in g]:
   if(V:=8 in g[-1]):g=g[::-1]
   for r in g:
    if r[0]:c+=1
    for j in range(len(r)):
     if g[0][max(0,j-c)]:r[j]=8
   if V:g=g[::-1]
 return g