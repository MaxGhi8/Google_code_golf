def p(h):
 (r,i,t),(n,l,m)=[(i,j,h)for i,r in enumerate(h)for j,h in enumerate(r)if h];f=i==l
 if f:*h,=map(list,zip(*h));r,i,n,l=i,r,l,n
 if i>l:r,i,t,n,l,m=n,l,m,r,i,t
 p=l-i>>1
 for r,i,g,t in(r,i,t,1),(n,l,m,-1):
  j=i+t*p-t;h[r][i:j+t:t]=[g]*p
  for k in-2,-1,1,2:u=h[r+k];u[j+t*(~k&1)]=u[j]=g
 return[*zip(*h)]*f or h