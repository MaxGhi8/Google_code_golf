def p(g,M=29,T=841):
 A=range;L=sum(g,[]);R=C=99;D={}
 for r in A(1,30):
  for c in A(1,30):
   d={}
   for k in A(T):
    if(v:=L[k])and d.setdefault(t:=k//M%r*c+k%M%c,v)-v:break
   else:
    if r*c<R*C:R,C,D=r,c,d
 for k in A(T):
  L[k]=L[k]or D.get(k//M%R*C+k%M%C,0)
 return[L[i:i+M]for i in A(0,T,M)]