def p(s,p=lambda s:[[t*(t<3)for t in t]for t in zip(*s)if 2in t]):
 for t in range(10-len(p:=p(p(s))),-1,-1):
  for n in range(11-len(p[0])):
   if sum(s[t+l][n+r]*p[l][r]for r in range(len(p[0]))for l in range(len(p)))<((t,n,s[len(p[0])+3][0])not in((1,3,0),(2,6,0))):
    for r in range(len(p[0])):
     for l in range(len(p)):s[t+l][n+r]|=p[l][r]
 return s