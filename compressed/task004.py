def p(p,u=enumerate):
 f={};s=len(p[0])
 for q,t in u(p[::-1]):
  for n,e in u(t[::-1]):
   if f.setdefault(e,(q,n))*e*(q-f[e][0])*(n-f[e][1]):t[s+~n]=0;t[s-n]=e
 return p