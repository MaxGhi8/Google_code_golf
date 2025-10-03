def p(y,s=5):
 for r in range(8):
  o=y[r+1];s+=sum(o)<1
  for f in range(1,9):
   if y[r+2][f+1]*y[r][f-1]*o[f-1]:o[f]=s
 a=sum(y,[]);o,a=sorted({*a},key=a.count)[:2];return[[{r:r,o:1,a:2}[r]for r in r]for r in y]
