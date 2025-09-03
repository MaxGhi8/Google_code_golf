def p(g,R=range,e=enumerate):
 h=[0]*(W:=len(g[m:=0]))
 for i,r in e(g):
  for j,v in e(r):h[j]=[0,h[j]+1][v<1]
  L,S=[-1]*W,[W]*W;s=[]
  for j,v in e(h):
   while s and h[s[-1]]>=v:s.pop()
   L[j]=s[-1]if s else-1;s+=j,
  s=[]
  for j,v in list(e(h))[::-1]:
   while s and h[s[-1]]>v:s.pop()
   S[j]=s[-1]if s else W;s+=j,
  for K,A,F in zip(h,L,S):
   if K>1<(a:=K*(F+~A))>m:m,Y,X=a,(-K-~i,-~i),(-~A,F)
 for y in R(*Y):
  for x in R(*X):g[y][x]=6
 return g
