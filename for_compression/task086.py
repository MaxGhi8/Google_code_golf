def p(g,E=enumerate):
 h,k,_=sorted({*(s:=sum(g,[]))},key=s.count)
 for I in'abcd':
  K=0;g=[*map(list,zip(*g))][::-1]
  for i,r in E(g):
   for j,v in E(r):
    if v==k:
     for a in range({4:3,2:0,7:min(3,2+(k<8or'c'!=I)*int(K:=K+.3))}.get(r.count(k),2)):g[i-a][j]=g[i-a][j]or h
 return[[*map({h:k,k:h}.get,r,r)]for r in g]