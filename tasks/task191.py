def p(g,R=range,E=enumerate):
 (y,x),*_,(Y,X)=[(i,j)for i,r in E(g)for j,v in E(r)if v%4]
 t=[r[x:X+1]for r in g[y:Y+1]];h=Y-y+1;w=X-x+1
 for q in R(12):
  for i in R(26-h):
   for j in R(26-w):k=[1];[exec('k[0]=0')for a in R(h-2)for b in R(w-2)if((u:=g[i+a][j+b])^4)*((v:=t[a+1][b+1])^1)|u*(v<4)];[exec('g[Y][X]|=t[a][b]&1')for a in R(h)for b in R(w)if 23>(Y:=i+a-1)>-1<(X:=j+b-1)<23*k[0]]
  t=[*zip(*t[::(-1,1,1)[q%3]])];h,w=w,h
 return g