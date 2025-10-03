def p(m):
 f=max(r:=m[0],key=r.count);x={};n=n=0
 for _ in[0]*4:
  for r in m:
   for c in{*r}-{f}:
    for e,y in enumerate(r[(i:=r.index(c)):]):
     if y!=c:break
    i=r[i+e:]
    try:s=i.index(c)
    except:s=0
    if(e,s)>x.get(c,(0,0)):x[c]=(e,s);n|=s>0;n|=1>s
  *m,=map(list,zip(*m[::-1]))
 i=sorted((s and s+e*2or(e>1)*n*n*3or e,e,s,c)for c,(e,s)in x.items());n=i[-1][0];m=[n*[f]for _ in[0]*n]
 for _ in[0]*4:
  for k,e,s,c in i:f=(n-k)//2;m[f][f+k-e:f+k]=m[f+k-1][f+k-e:f+k]=[c]*e
  *m,=map(list,zip(*m[::-1]))
 return m