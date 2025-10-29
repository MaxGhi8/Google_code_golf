def p(g):
 i=j=0
 for r in g:
  if 4in r:i,j=[(0,0),filter(r.__getitem__,range(10))][i==j]
  else:r[-~i:j]=[2]*(j+~i)
 return g
