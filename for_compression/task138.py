def p(r):
 for a in range(8):
  *r,=map(list,zip(*r[::-1]));r=r[:max(i+1for i,a in enumerate(r)if all(a))]
  for i,a in enumerate(r[2:-1]*(a>3)*(max(max(a[1:-1]for a in r[1:-1]))==r[-1][1]),2):a[:]=map(max,a,r[i-1])
 return r
