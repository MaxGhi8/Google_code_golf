def p(g,c=1,R=range,A=0,L=len):
 for a,*x,Y,h in sorted((-h*k,a,a+k,b,h)for a in R(L(g))for b in R(L(g[0]))for k in R(-a-~L(g))for h in R(-b-~L(g[0]))if all(sum(r[b:b+h])<1for r in g[a:a+k])):
  if a>A:return p(g,c+2)
  for i in R(*x):g[i][Y:Y+h]=[c]*h;A=a
 return[[{1:1,2:2,c-2:8}.get(v,0)for v in r]for r in g]