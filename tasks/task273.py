def p(g):
 i=j=0
 for r in g:
  if 4in r:i,j,*_=[(0,0),filter(r.__getitem__,range(10))][max(i,j)==0]
  else:r[i+1:j]=[2]*(j+~i)
 return g
