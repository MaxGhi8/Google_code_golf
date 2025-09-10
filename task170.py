def p(g,e=enumerate,f=lambda d:[*filter(any,zip(*d))],L=len):
 t=sum(g,[])[::-1];i=[i for i,v in e(t)if v][0];n=L(g[0])
 while t[i]:i-=~n;x=L(t)-i;G=g[x//n:];C=f(f(r[x%n:]for r in G))
 for r in G:r[x%n:]=[0]*(n-x%n)
 l=L(K:=f(f(g)))//L(C);return[[K[i*l][j*l]and v for j,v in e(r)]for i,r in e(C)]