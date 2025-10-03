def p(m):
 b=max(r:=m[0],key=r.count);d={};n=t=0
 for _ in[0]*4:
  for r in m:
   for c in{*r}-{b}:
    for e,u in enumerate(r[(o:=r.index(c)):]):
     if u!=c:break
    i=r[o+e:]
    try:s=i.index(c)
    except:s=0
    if(e,s)>d.get(c,(0,0)):d[c]=(e,s);n|=s>0;t|=1>s
  *m,=map(list,zip(*m[::-1]))
 i=sorted((s and s+e*2or(e>1)*n*t*3or e,e,s,c)for c,(e,s)in d.items());n=i[-1][0];m=[n*[b]for _ in[0]*n]
 for _ in[0]*4:
  for w,e,s,c in i:b=(n-w)//2;m[b][b+w-e:b+w]=m[b+w-1][b+w-e:b+w]=[c]*e
  *m,=map(list,zip(*m[::-1]))
 return m