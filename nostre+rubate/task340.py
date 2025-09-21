def p(g):
 D=[]
 for _ in[0]*4:
  *g,=map(list,zip(*g[::-1]))
  for r in g[1:-1]:
   D+=[C:=r[0]]
   if C in r[1:]:r[r[1:].index(C)+1]=0;r[1]=C
 return[[c*(c in D)for c in r]for r in g]