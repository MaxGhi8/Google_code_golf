def p(g,p=lambda g:[*zip(*filter(any,g))]):
 k=v=-1
 for _ in'0'*96:
  *g,=map(list,zip(*[[r[j]or(r[:j].count(c:=max(sum(g,[])))==1)*k*(c in r[j:]or r[j-1]==k)for j in range(len(g))]for r in g[::-1]]));v+=(v<0<('0'in str(p(p(g)))))^1;*_,r=filter(any,g)
  if v%4==0<v:
   if(I:=r.index(k)-v//4)>k:r[I]=k
   if(I:=v//4+~r[::-1].index(k))<0:r[I]=k
   v*=k**(g[-1]==r)
 return[[*map({k:4}.get,r,r)]for r in g]
