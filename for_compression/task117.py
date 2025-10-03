def p(g):
 s=sum(g,[]);b=len(g);i=max(i for i in range(b*b+~b)if(s[i-~b]==s[i]==s[i+~b]==s[i-b+1]==s[i+b-1])*s[i]);a,b=divmod(i,b);h=({*s}-{0,s[i]}).pop()
 for y,r in enumerate(g):
  for x,v in enumerate(r):
   if v==h:(m:=g[2*a-y])[x]=r[2*b-x]=m[2*b-x]=h
 return g