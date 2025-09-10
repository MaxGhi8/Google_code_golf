def p(g):
 for _ in 0,1:
  g=g[::-1];I=sum(g,[]).index(5)//10
  for a in range(I*10):g[i][j]=2*(2in[*zip(*g[:(i:=a//10)+1])][j:=a%10])+(1in[*zip(*g[i:I])][j])
 return g