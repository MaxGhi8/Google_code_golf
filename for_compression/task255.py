def p(g):
 for *b,p,d,a,b in sorted((-sum(sum([r[b:b+p]for r in g[a:a+d]],[])),p*d,p,d,a,b)for a in range(22)for b in range(22)for d in range(5,31-a)for p in range(5,31-b))[-22:]:
  for i in range(a+1,a+d-1):
   for j in range(b+1,b+p-1):g[i][j]=3
 for b in' '*8:
  g=[*map(list,zip(*g[::-1]))]
  for i in range(30):
   for j in range(22):
    if g[i][j]==3and{*sum([*zip(*g[max(0,i-1):i+2])][j:],())}<={0,3}:g[i][j:]=[3]*len(g[i][j:])
 return g