def p(g,x=[5]*2):
 s=sum(g,[]);n=len(g)
 for i in range(n*n):g[i//n][i%n]=s[i]+(s[i::n+1][1:3]==x)+(s[i::n-1][1:3]==x)*2+(s[i::-n+1][1:3]==x)*3+(s[i::-n-1][1:3]==x)*4
 return g