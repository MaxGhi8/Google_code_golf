def p(g):
 i=j=0
 for r in g:
  if 4in r:i,j,*_=[(0,0),sorted(range(10),key=r.__getitem__,reverse=True)][max(i,j)==0]
  else:r[i+1:j]=[2]*(j+~i)
 return g
