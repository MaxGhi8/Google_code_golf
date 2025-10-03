def p(l):
 (m,f,u),(z,e,p)=[(i,p,z)for i,m in enumerate(l)for p,z in enumerate(m)if z];i=f==e
 if i:*l,=map(list,zip(*l));m,f,z,e=f,m,e,z
 if f>e:m,f,u,z,e,p=z,e,p,m,f,u
 d=e-f>>1
 for m,f,u,i in(m,f,u,1),(z,e,p,-1):
  p=f+i*d-i;l[m][f:p+i:i]=[u]*d
  for e in-2,-1,1,2:z=l[m+e];z[p+i*(~e&1)]=z[p]=u
 return[*zip(*l)]*i or l