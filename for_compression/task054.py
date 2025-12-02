def p(b):
 f=b[0][0];d,*n=[*map(list,b)],
 for y in range(30):
  for x in range(30):
   if d[y][x]-f:
    d[y][x]=f;q=[(y,x)]
    for Y,o in q:
     for i in-1,0,1:
      for j in-1,0,1:
       ny,nx=Y+i,o+j
       if(i+j)*(30>ny>-1<nx<30)and d[ny][nx]-f:d[ny][nx]=f;q+=[(ny,nx)]
    n+=q,
 t=min((o for o in n if o[1:]),key=len)
 C,g=map(lambda z:(min(z)+max(z))>>1,zip(*t));s={(y-C,x-g):b[y][x]for y,x in t}
 for y,x in[(y,x)for y in range(30)for x in range(30)if b[y][x]==b[C][g]*(not(y,x)in t)]:
  for(i,j),h in s.items():
   for p in range(1,2+30*((i*(j+2),j<<1)in s)):
    ny,nx=y+i*p,x+j*p
    if not(30>ny>-1<nx<30and b[ny][nx]!=f):break
    b[ny][nx]=h
 for y,x in t:b[y][x]=f
 return b