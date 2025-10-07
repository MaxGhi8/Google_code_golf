def p(g,i=lambda g:[*zip(*filter(lambda r:0in r,g))]):
 t=i(i(g));n=len(t);l,={*sum(g,[])}-{0,(K:=sum(g,[])[0])};N=len(g[0])
 for i in range(4):
  g=[r[::(1,-1)[i%2]]for r in g[::(-1,1)[i%2]]];i,y=divmod(sum(g,[]).index(l),N);A,B=divmod(sum(g,[]).index(0),N)
  X,Y=zip(*[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v<1]);a,e=min(X),max(X);c,d=min(Y),max(Y);o=g[a][c]==K
  if(e<=i)*(d<y):
   a+=i-A;c+=y-B
   while(a<len(g))*(c<N):
    for i in range(n):
     for j in range(n):
      if(a+i<len(g))*(c+j<N):g[a+i][c+j]=[K,l][t[i][j]<1]
    a+=n-o;c+=n-o
 return g