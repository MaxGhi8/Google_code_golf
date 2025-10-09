def p(p):
 for *n,m,n,a,z in sorted((-sum(sum([a[z:z+m]for a in p[a:a+n]],[])),m*n,m,n,a,z)for a in range(22)for z in range(22)for n in range(5,31-a)for m in range(5,31-z))[-22:]:
  for a in range(a+1,a+n-1):
   for n in range(z+1,z+m-1):p[a][n]=3
 for n in' '*8:
  p=[*map(list,zip(*p[::-1]))]
  for a in range(30):
   for n in range(22):
    if p[a][n]==3and{*sum([*zip(*p[max(0,a-1):a+2])][n:],())}<={0,3}:p[a][n:]=[3]*len(p[a][n:])
 return p