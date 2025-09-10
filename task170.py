def p(g,e=enumerate,f=lambda d:[*filter(any,zip(*d))]):
 t=sum(g,[])[::-1];i=[i for i,v in e(t)if v][0];n=len(g[0])
 while t[i]:i-=~n;x=len(t)-i;b=x%n;G=g[x//n:];C=f(f(r[b:]for r in G))
 for r in G:r[b:]=[0]*(n-b)
 l=len(K:=f(f(g)))//len(C);return[[K[i*l][j*l]and v for j,v in e(r)]for i,r in e(C)]