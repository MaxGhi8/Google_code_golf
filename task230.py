def p(g):
 s=sum(g,[]);n=len(g)
 for i in range(n*n):e=lambda k:s[i::k][1:3]==[5]*2;g[i//n][i%n]=s[i]+e(n+1)+e(n-1)*2+e(1-n)*3+e(-1-n)*4
 return g