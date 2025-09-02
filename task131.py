def p(g):
 for _ in[0]*4:
  m=len(g[0]);n=len(g);s=sum(g,[]);a=s.index(2)//m;b=s.index(3)//m;d=n-s[::-1].index(3)//m
  if m<n and b>a:g=g[:a+1]+g[b:d]+[[8]*m]+[[0]*m]*(n-a+b-d-2)
  g=[*map(list,zip(*g[::-1]))]
 return g