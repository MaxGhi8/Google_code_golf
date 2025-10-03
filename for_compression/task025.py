def p(e,p=lambda f:[*zip(*f)]):
 e=(p(e),e)[t:=1-any(a&n for a,n,*y in e)];a=[[0]*-~-~len(p(e))for y in e]
 for n,y in enumerate(p(e)):
  for u,y in[*enumerate(y)]*all(y):a[u][n:n+3]=y*(y in e[u][:n]),y,y*(y in e[u][n+1:])
 return[a:=p(a)[1:-1],p(a)][t]
