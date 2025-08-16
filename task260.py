def p(g,E=enumerate):
 k,*_=set(sum(g,[]))-{0,5};n=len(g)
 L=[(i,n-j-1)for i,r in E(g)for j,v in E(r[::-1])if v==5and not r.__setitem__(n-j-1,0)];p,q,r,s=L[0]+L[-1]
 M=[r[:] for r in g]
 if k in g[p][:q]:
  d=min(q+1,p-1);p-=d+1;q-=d-1
  while(p<n)*(q<n):M[p][q]=k;p+=1;q+=1
 if k in g[r][s:]:
  d=min(r+1,s-1);r-=d-1;s-=d+1
  while(r<n)*(s<n):M[r][s]=k;r+=1;s+=1
 return M