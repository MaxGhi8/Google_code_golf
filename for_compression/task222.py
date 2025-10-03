def p(y):
 for s,e in enumerate(y):
  for b,o in enumerate(e):
    if (sum(e[b-1:b+2].count(o)for e in y[s-1:s+2])>3)*(o in e[b-1:b+2:2])*(o in{e[b]for e in y[s-1:s+2:2]})<1:e[b]=0
 o=max({*(x:=sum(y,[]))}-{0},key=x.count);return[[o*(o==o)for o in e]for e in y]