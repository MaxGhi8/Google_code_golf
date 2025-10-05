def p(l,m=2):
 *l,=map(list,zip(*l[::-1]));s=0
 if 2 not in l[0]+l[-1]+[t[-1]for t in l]:
  if(o:=8 in l[-1]):l=l[::-1]
  for t in l:
   if t[0]:s+=1
   for f in range(len(t)):
    if l[0][max(0,f-s)]:t[f]=8
  if o:l=l[::-1]
 return-m*l or p(l,m-1)