def p(g):
 k=max(r:=g[0],key=r.count);e={};o=a=0
 for _ in[0]*4:
  for r in g:
   i=0;s=len(r)
   while s>i:
    t=r[i]
    if t==k:i+=1;continue
    d=i
    while s>d and r[d]==t:d+=1
    i=d-i;z=d
    while s>z and r[z]!=t:z+=1
    c=s>z and z-d
    if(i,c)>e.get(t,(0,0)):e[t]=(i,c);o|=c>0;a|=2>i and 1>c
    i=d
  *g,=map(list,zip(*g[::-1]))
 r=sorted((c and c+i*2or i>1and o*a*3or i,i,c,t)for t,(i,c)in e.items());n=r[-1][0];g=[n*[k]for _ in[0]*n]
 for _ in[0]*4:
  for d,i,c,t in r:o=(n-d)//2;g[o][o+d-i:o+d]=g[o+d-1][o+d-i:o+d]=[t]*i
  *g,=map(list,zip(*g[::-1]))
 return g