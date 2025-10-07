def p(g):
 (y,x),*_,(Y,X)=[(i,j)for i,q in enumerate(g)for j,v in enumerate(q)if v%4]
 t=[q[x:X+1]for q in g[y:Y+1]];h=Y-y+1;w=X-x+1
 for q in range(26):
  for i in range(26-h):
   for j in range(26-w):
    o=1
    for a in range(h-2):
     for e in range(w-2):
      if((u:=g[i+a][j+e])^4)*((v:=t[a+1][e+1])^1)|u*(4>v):o=0
    for a in range(h):
     for e in range(w):
      if(23>(Y:=i+a-1)>=0)*(23>(X:=j+e-1)>=0)*o:g[Y][X]|=t[a][e]&1
  t=[*zip(*t[::(-1,1,1)[q%3]])];h,w=w,h
 return g