def p(g):
 j=sum(g,[]);e=len(g);i=max(i for i in range(e*e+~e)if(j[i-~e]==j[i]==j[i+~e]==j[i-e+1]==j[i+e-1])*j[i]);s,e=divmod(i,e);h=({*j}-{0,j[i]}).pop()
 for n,i in enumerate(g):
  for x,l in enumerate(i):
   if l==h:(f:=g[2*s-n])[x]=i[2*e-x]=f[2*e-x]=h
 return g
