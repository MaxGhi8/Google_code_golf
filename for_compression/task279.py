def p(r):
 def p(s,j,a,b,e):
  e|={(s,j)}
  for u,l in(1,0),(-1,0),(0,1),(0,-1):
   if len(r)>(u:=s+u)>-1<(l:=j+l)<len(r[0])and 2>r[u][l]and(u-a|l-b)and((u,l)in e or p(u,l,s,j,e)):return 7
  return 0
 return[[r+p(s,j,-1,-1,set())*(2>r)for j,r in enumerate(r)]for s,r in enumerate(r)]