def p(w):
 x,*l={(n,h)for n,p in enumerate(w)for h,l in enumerate(p)if l},
 def p(f):
  if f in x:x.remove(f);n.add(f);[p((f[0]+h//3-1,f[1]+h%3-1))for h in range(9)]
 while x:l+=[n:=x-x];p(min(x))
 for f in range(len(w)):
  for n in range(len(w)):
   for x in range(6):
    if x in[-(min([*zip(*o)][1])-max([*zip(*o)][1])>>1)for h in range(-x,x+1)for p in range(-x,x+1)for o in l if(f+h,n+p)in o]:w[f][n]=w[f][n]or 3
 return[[l or 9in h[:f]for*h,l in zip(*w,n)]for f,n in enumerate(w)]