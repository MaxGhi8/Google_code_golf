def p(g):
 for _ in 0,1:
  g=g[::-1];I=sum(g,[]).index(5)//10
  for a in range(I*10):i,j=divmod(a,10);g[i][j]=2*(2in[*zip(*g[:i+1])][j])+(1in[*zip(*g[i:I])][j])
 return g