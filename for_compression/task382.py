def p(r):
 for d in' '*4:
  *r,=map(list,zip(*r[::-1]));o=0
  if 2 not in r[0]+r[-1]+[a[-1]for a in r]:
   if(d:=8 in r[-1]):r=r[::-1]
   for a in r:
    if a[0]:o+=1
    for t in range(len(a)):
     if r[0][max(0,t-o)]:a[t]=8
   if d:r=r[::-1]
 return r