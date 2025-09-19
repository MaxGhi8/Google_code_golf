def p(g,R=lambda g:[*map(list,zip(*g))][::-1]):
 s=sum(g,[]);b=R(a:=R(g));g=[[*map(sum,zip(*r))]for r in zip(g,a,b,R(b))]
 for _ in' '*4:
  for k in(g:=R(g))[1][1]*[x for x in s if s.count(x)>1]:r,x=[(r,r.index(k))for r in g if k in r][0];r[x:19-x:2]=[k]*(10-x)
 return g