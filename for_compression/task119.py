def p(s,u=2):
 *s,=map(list,zip(*s[::-1]))
 if 2 not in s[0]:
  n=[n for n in range(12)if any(s[n])][0];i=1
  for y in range(1,12):
   if 8in[*zip(*s)][-1]:y=~y
   if s[n:=n+i][y]==2:i=-1;n+=2*i
   s[n][y]=s[n][y]or 3
 return-u*s or p(s,u-1)