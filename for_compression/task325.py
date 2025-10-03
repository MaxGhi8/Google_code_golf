def p(g):
 f,o,p=len(g),len(g[0]),0
 def n(i,u):
  g[i][u]=0
  for d,e in(1,0),(-1,0),(0,1),(0,-1):
   if f>(d:=i+d)>-1<(e:=u+e)<o and g[d][e]:n(d,e)
 for i in range(f*o):
  if g[r:=i//o][e:=i%o]:p+=1;n(r,e)
 return[[0]*i+[8]+[0]*(p+~i)for i in range(p)]