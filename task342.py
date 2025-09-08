def p(g):
 i,j=divmod(sum(g,[]).index(8),10);f=lambda s:(max(max(r[:j])for r in s),max(max(r[j+2:])for r in s));m=[[0]*10 for _ in' '*10];m[i][j:j+2],m[i+1][j:j+2]=map(f,(g[:i],g[i+2:]));return m