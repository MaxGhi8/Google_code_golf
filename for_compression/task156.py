def p(g,C=5):
 for r in range(8):
  t=g[r+1];C+=sum(t)<1
  for c in range(1,9):
   if g[r+2][c+1]*g[r][c-1]*t[c-1]:t[c]=C
 f=sum(g,[]);a,b=sorted({*f},key=f.count)[:2];return[[{x:x,a:1,b:2}[x]for x in r]for r in g]