def p(g):
 i=j=r=0;X=[0,1,0,-1];n=len(g)
 while r<99:g[i][j]=3;x=X[r&3];y=X[(r+1)&3];a=i+x;b=j+y;i,j,r=[(i,j,r+1),(a,b,r)][r<3<n>a>=0<=b<n or r>2and g[a+x][b+y]<1]
 return g