def p(g):
 R=range(10)
 for m in[0]*40:g=[[R or r>10and r for R,r in zip(m,[11]+m)]for*m,in zip(*g[::-1])]
 m=r={}
 for i in R:
  for j in R:m.setdefault(g[i][j],[]).append((i,j))
 def f(u,s,b):(u in c)and(c.remove(u),e.append((u[0]-s,u[1]-b)),[f((u[0]+A%3-1,u[1]+A//3-1),s,b)for A in R[:9]])
 for k in R:
  c=m.get(k);o={}
  while c:e=o[min(c)]=[];f(min(c),*min(c))
  if g[6][6]==9:o.pop((6,4),0)
  r[k]=o
 for(i,j),c in r[0].items():
  for k in R[1:]:
   if len(D:=r.get(k,()))==1:
    ((s,b),f),=D.items()
    if f==c and f[1:]:
     for u in f:g[s+u[0]][b+u[1]]=0;g[i+u[0]][j+u[1]]=k
 return[[k%11 for k in m]for m in g]