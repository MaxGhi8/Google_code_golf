def p(g,r=range):
 h=-~(W:=len(g[m:=0]))*[m]
 for i in r(len(g)):
  s=[-1]
  for j in r(-~W):
   if j<W:h[j]=(g[i][j]<1)*-~h[j]
   while-~s[-1]*(h[s[-1]]>=h[j]):
    if(K:=h[s.pop()])>1<(a:=K*(j+~s[-1]))>m:m,A,B,C,D=a,-K-~i,-~i,-~s[-1],j
   s+=j,
 for y in r(A,B):g[y][C:D]=[6]*(D-C)
 return g
