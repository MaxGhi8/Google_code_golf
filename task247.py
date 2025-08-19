def p(g):
 D={x:sum(g,[]).count(x)for x in range(1,10)};L=max(D.values());m=[[]]*L
 for c in zip(*g):
  for k in{*c}:
   if D.pop(k,0)==L:m=[r+[k]for r in m]
 return m