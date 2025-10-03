def p(g,c=1,A=0):
 for a,*x,Y,h in sorted((-h*k,a,a+k,b,h)for a in range(len(g))for b in range(len(g[0]))for k in range(-a-~len(g))for h in range(-b-~len(g[0]))if all(sum(r[b:b+h])<1for r in g[a:a+k])):
  if a>A:return p(g,c+2)
  for i in range(*x):g[i][Y:Y+h]=[c]*h;A=a
 return[[{1:1,2:2,c-2:8}.get(v,0)for v in r]for r in g]