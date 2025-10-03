def p(l):
 e=len(l[0]);n=sum(l,[]);l=len(n);r=[n.index(2)];u=l+~n[::-1].index(2)
 while r:
  if(p:=r.pop())==u:return[[8]]
  n[p]=0;r+=[i for d in(p%e<e-1,-(p%e>0),e,-e)if-1<(i:=p+d)<l and n[i]]
 return[[0]]
