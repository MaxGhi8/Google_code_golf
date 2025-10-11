def p(n):
 P,*e={(r,c)for r,g in enumerate(n)for c,v in enumerate(g)if v},
 def B(z):
  if z in P:P.remove(z);C.add(z);[B((z[0]+A//3-1,z[1]+A%3-1))for A in range(9)]
 while P:e+=[C:=P-P];B(min(P))
 for i in range(len(n)):
  for j in range(len(n)):
   for d in range(6):
    if d in[-(min([*zip(*o)][1])-max([*zip(*o)][1])>>1)for A in range(-d,d+1)for B in range(-d,d+1)for o in e if(i+A,j+B)in o]:n[i][j]=n[i][j]or 3
 return[[v or 9in c[:i]for*c,v in zip(*n,r)]for i,r in enumerate(n)]