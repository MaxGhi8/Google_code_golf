def p(t):
 d,g,*a={(d,n):l for d,f in enumerate(t)for n,l in enumerate(f)if l},1,
 def p(z):
  if z in d:t,y=z;f.add((t-x[0],y-x[1],d.pop(z)));[p((t+d%3-1,y+d//3-1))for d in range(9)]
 for x,i in[*d.items()]:
  if i==2:a+=[(x,f:=set())];p(x);g=[g,f][any(l&1for*t,l in f)]
 r={z for z in g if z[2]&1};z=g-r;g=1,-1;y=lambda x,*d:(d[x&1]*g[x&2>0],d[1^x&1]*g[x&4>0])
 for(i,p),m in a:
  for x in range(9):
   for*d,l in[*r]*({(*y(x,*d),l)for*d,l in z}==m):f,m=y(x,*d);t[f+i][m+p]=l
 return t