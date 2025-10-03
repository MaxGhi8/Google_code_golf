def p(g,c=1,m=0):
 for a,*u,Y,h in sorted((-h*k,a,a+k,b,h)for a in range(len(g))for b in range(len(g[0]))for k in range(-a-~len(g))for h in range(-b-~len(g[0]))if all(sum(r[b:b+h])<1for r in g[a:a+k])):
  if a>m:return p(g,c+2)
  for i in range(*u):g[i][Y:Y+h]=[c]*h;m=a
 return[[{1:1,2:2,c-2:8}.get(h,0)for h in r]for r in g]