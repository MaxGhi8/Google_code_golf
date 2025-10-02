def p(g,c=1):
 for _ in' '*4:
  g=[*zip(*g)][::-1]
  if c and{*sum(g[(a:=sum(g,()).index(8)//len(g[0])):],())}=={0,8}:
   for i in range(max(i for i in range(a)if sum(g[i])),a):g[i:i+2]=g[i-1:i+1];c=0
 return g