def p(g):
 (y,x),*_,(Y,X)=[(i,j)for i,r in enumerate(g)for j,v in enumerate(r)if v%4]
 t=[r[x:X+1]for r in g[y:Y+1]];h=Y-y+1;w=X-x+1
 for q in range(26):
  for i in range(26-h):
   for j in range(26-w):
    k=1
    for a in range(h-2):
     for b in range(w-2):
      if((u:=g[i+a][j+b])^4)*((v:=t[a+1][b+1])^1)|u*(4>v):k=0
    for a in range(h):
     for b in range(w):
      if(23>(Y:=i+a-1)>=0)*(23>(X:=j+b-1)>=0)*k:g[Y][X]|=t[a][b]&1
  t=[*zip(*t[::(-1,1,1)[q%3]])];h,w=w,h
 return g