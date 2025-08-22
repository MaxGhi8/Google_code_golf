def p(g,f=lambda m:[*map(list,zip(*m))]):
 E=[]
 for c in f(g):
  if(k:=sum(c)//4):c[-k:]=[8]*k
  E+=[c]
 return f(E)