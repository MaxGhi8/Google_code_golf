def p(g,f=lambda g:map(list,zip(*g[::-1]))):
 b=max(r:=g[0],key=r.count);d={};A=B=0
 for _ in[0]*4:
  for r in g:
   for c in{*r}-{b}:
    for L,s in enumerate(r[(x:=r.index(c)):]):
     if s!=c:break
    t=r[x+L:]
    try:S=t.index(c)
    except:S=0
    if(L,S)>d.get(c,(0,0)):d[c]=(L,S);A|=S>0;B|=L<2>1>S
  *g,=f(g)
 T=sorted((S and S+L*2or(L>1)*A*B*3or L,L,S,c)for c,(L,S)in d.items());n=T[-1][0];R=[n*[b]for _ in[0]*n]
 for _ in[0]*4:
  for w,L,S,c in T:o=n-w>>1;R[o][o+w-L:o+w]=R[o+w-1][o+w-L:o+w]=[c]*L
  *R,=f(R)
 return R