def p(l,u=lambda l:[*map(list,zip(*l))][::-1]):
 s=sum(l,[]);i=u(p:=u(l));l=[[*map(sum,r)]for r in map(zip,l,p,i,u(i))]
 for r in' '*4:
  for p in(l:=u(l))[1][1]*[a for a in s if s.count(a)>1]:r,a=[(r,r.index(p))for r in l if p in r][0];r[a:19-a:2]=[p]*(10-a)
 return l