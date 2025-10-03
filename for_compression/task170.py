def p(l,f=lambda n:[*filter(any,zip(*n))]):
 t=sum(l,[])[::-1];i=[i for i,s in enumerate(t)if s][0];p=len(l[0])
 while t[i]:i-=~p;n=len(t)-i;r=l[n//p:];m=f(f(r[n%p:]for r in r))
 for r in r:r[n%p:]=[0]*(p-n%p)
 l=len(e:=f(f(l)))//len(m);return[[e[i*l][r*l]and s for r,s in enumerate(r)]for i,r in enumerate(m)]
