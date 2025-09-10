def p(g):
 w=len(g[0]);t=sum(g,[]);m=len(t);q=[t.index(2)];b=m+~t[::-1].index(2)
 while q:
  if(x:=q.pop())==b:return[[8]]
  t[x]=0;q+=[k for a in(x%w<w-1,-(x%w>0),w,-w)if-1<(k:=x+a)<m and t[k]]
 return[[0]]