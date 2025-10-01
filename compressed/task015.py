def p(r):
 for u in range(576):c,k,j=u//72,u//9%8,u%3-1;u%=9;b=u//3-1;r[c+b][k+j]=u%2*7*((d:=r[c][k])==1)or r[c+b][k+j]or(u%2<1)*4*(d==2)
 return r