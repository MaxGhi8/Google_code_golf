def p(g,e=enumerate):
 D=[]
 for i in'    ':
  g=[*map(list,zip(*g[::-1]))]
  for i,r in e(g[1:-1],1):
   D+=[C:=r[0]]
   if C in r[1:]:r[r[1:].index(C)+1]=0;r[1]=C
 return[[c*(c in D)for c in r]for r in g]