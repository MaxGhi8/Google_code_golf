def p(g,r=range,e=enumerate):
 h=[0]*(W:=-~len(g[m:=0]))
 for i,R in e(g):
  for j,v in e(R):h[j]=v<1and h[j]+1;s=[-1]
  for j in r(W):
   while-~s[-1]and h[s[-1]]>=h[j]:
    K=h[s.pop()];a=K*(j+~s[-1])
    if 1<K<a>m:m,A,B,C,D=a,-K-~i,-~i,-~s[-1],j
   s+=j,
 for y in r(A,B):g[y][C:D]=[6]*(D-C)
 return g