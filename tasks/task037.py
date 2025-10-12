def p(g):
 for _ in' '*10:
  for i in range(11,100):
   if 0<(s:=sum(g:=g[::-1],[]))[i-11]in s[i::11]:g[i//10][i%10]=s[i-11]
 return g