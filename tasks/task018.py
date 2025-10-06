def p(q,E=enumerate):
 L=sum(q,[]);K=max(range(1,10),key=L.count);A=({*L}-{0,K}).pop()
 d,*j={(d,n):e for d,f in E(q)for n,e in E(f)if e},
 def B(z):
  if z in d:x,y=z;C.add((x-X,y-Y,d.pop(z)));[B((x+A%3-1,y+A//3-1))for A in range(9)]
 for(X,Y),v in[*d.items()]:
  if v==A:
   C=set();B((X,Y))
   if len(C)>3:
    j+=[C]
    for a,b,_ in C:q[a+X][b+Y]=0
 o=1,-1;y=lambda k,*d:(d[k&1]*o[k&2>0],d[1^k&1]*o[k&4>0])
 for X,R in E(q):
  for Y,v in E(R):
   for J in[*j]*(v==A):
    for Q in range(9):
     try:
      if sum(u==q[X+y(Q,t,p)[0]][Y+y(Q,t,p)[1]]!=K for t,p,u in J)>2:
       for t,p,u in J:f,m=y(Q,t,p);q[f+X][m+Y]=q[f+X][m+Y]or K
     except:0
 return q