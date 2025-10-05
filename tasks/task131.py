def p(g,k=2):
 m=len(g[0]);n=len(g);s=sum(g,g[0]*0);a=s.index(2)//m;b=s.index(3)//m;d=n-s[::-1].index(3)//m
 if m<n and b>a:g=g[:a+1]+g[b:d]+[[8]*m]+[[0]*m]*(n-a+b-d-2)
 *g,=zip(*g[::-1])
 return-k*g or p(g,k-1)