def p(g):
 i=j=r=0;X=[0,1,0,-1];Y=X[1:]+[0]
 while r<99:g[i][j]=3;x=X[r%4];y=Y[r%4];I=i+x;J=j+y;i,j,r=[(i,j,r+1),(I,J,r)][r<3<len(g)>I>=0<=J<len(g)or r>2and g[I+x][J+y]<1]
 return g