def p(g,R=range,Z=zip,A=any):
 x=i=0
 while 1:
  if A(g[i:=i+1]):x=x or i
  elif x:break
 w=len(m:=g[x-1:i+1])
 for j in R(14):
  if A(map(A,x:=g[j:j+w]))&(sum(x[0]+x[-1])<1):
   i=9-min([*r[::-1],8].index(8)for r in x)
   for b in 0,-1,1,-2:
    if(i-~b)*all(i==b for i,b in Z([*Z(*m)][i+b::-1],[*Z(*x)][i::-1])):[g[j+k].__setitem__(a,x[k][a]or a+b<10and m[k][a+b]>1)for k in R(w)for a in R(i+1,10)];break
 return g
