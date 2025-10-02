def p(g):
 b=max(r:=g[0],key=r.count);d={};A=B=0
 for _ in[0]*4:
  for r in g:
   i=0;N=len(r)
   while i<N:
    c=r[i]
    if c==b:i+=1;continue
    j=i
    while j<N and r[j]==c:j+=1
    L=j-i;h=j
    while h<N and r[h]!=c:h+=1
    S=h<N and h-j
    if(L,S)>d.get(c,(0,0)):d[c]=(L,S);A|=S>0;B|=L<2and S<1
    i=j
  *g,=map(list,zip(*g[::-1]))
 T=sorted((S and S+L*2or L>1and A*B*3or L,L,S,c)for c,(L,S)in d.items());n=T[-1][0];R=[n*[b]for _ in[0]*n]
 for _ in[0]*4:
  for w,L,S,c in T:o=(n-w)//2;R[o][o+w-L:o+w]=R[o+w-1][o+w-L:o+w]=[c]*L
  *R,=map(list,zip(*R[::-1]))
 return R