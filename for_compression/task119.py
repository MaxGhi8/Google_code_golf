def p(l):
 for r in ' '*4:
  *l,=map(list,zip(*l[::-1]))
  if 2 not in l[0]:
   r=[r for r in range(12)if any(l[r])][0];o=1
   for t in range(1,12):
    if 8in[*zip(*l)][-1]:t=~t
    if l[r:=r+o][t]==2:o=-1;r+=2*o
    l[r][t]=l[r][t]or 3
 return l