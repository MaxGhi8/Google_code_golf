def p(g,x=lambda g:[*zip(*filter(lambda r:0in r,g))]):
 t=x(x(g));S=sum(g,[]);K=S[0];n=len(t);k,={*S}-{0,K};N=len(g[0]);M=len(g);E=enumerate;D=divmod;R=range
 for i in R(4):
  g=[r[::1-2*(i&1)]for r in g[::2*(i&1)-1]];*S,=sum(g,[]);I=S.index;x,y=D(I(k),N);A,B=D(I(0),N)
  X,Y=zip(*[(i,j)for i,r in E(g)for j,v in E(r)if v<1]);a,b=min(X),max(X);c,d=min(Y),max(Y);o=g[a][c]==K
  if(x>=b)*(y>d):
   a+=x-A;c+=y-B
   while(a<M)*(c<N):
    for i in R(n):
     for j in R(n):
      if(a+i<M)*(c+j<N):g[a+i][c+j]=[K,k][t[i][j]<1]
    a+=n-o;c+=n-o
 return g