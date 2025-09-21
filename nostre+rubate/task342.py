def p(g):
 i,j=divmod(sum(g,[]).index(8),10);x=max;m=[[0]*10 for _ in g];m[i][j:2+j],m[i+1][j:2+j]=((x(x(r[:j])for r in s),x(x(r[j+2:])for r in s))for s in(g[:i],g[i+2:]));return m