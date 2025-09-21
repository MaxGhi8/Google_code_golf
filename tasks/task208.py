def p(g):
 s,t=divmod(440-(m:=sum(g,[]))[::-1].index(k:=min(m,key=m.count))-m.index(k),21)
 for i in range(21-s):
  for j in range(21-t):
   if sum(sum(r[j+1:j+t])for r in g[i+1:i+s])<1:
    g[i][j:j-~t]=g[i+s][j:j-~t]=[k]*-~t
    for r in g[i:i-~s]:r[j]=r[j+t]=k
 return g