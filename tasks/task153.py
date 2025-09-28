def p(g):
 s=sum(g,[]);h,k=sorted({*s}-{0},key=s.count)
 for s in'  ':g=[[v or h for v in r]for*r,in zip(*g)if k in r]
 for _ in'  ':
  if len(g:=[*zip(*g)])<3:g[:2-2*(h in g[0])]+=[[h]*3]
 return g