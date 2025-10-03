def p(g):
 def e(p,n,g):
  g[p][n]=1
  return 1+sum((10>(m:=p+a)>-1<(d:=n+r)<10 and g[m][d]<1 and e(m,d,g))for a,r in((1,0),(-1,0),(0,1),(0,-1)))
 return[[g[p][n]or 4-e(p,n,[*map(list,g)])for n in range(10)]for p in range(10)]