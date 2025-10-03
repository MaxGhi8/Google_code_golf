def p(g):
 d=[];e=[]
 for r in zip(*g):
  if sum(r):e+=r,
  else:d+=e,;e=[]
 if e:d+=e,
 for t,z in zip(d,d[1:]):
  e=(z[0].index(5)-t[-1].index(5))%3;z[:]=[r[e:]+r[:e]for r in z]
 return[sum(r,[])for r in zip(*[[[*map({5:max({*sum(e,())}-{0,5})}.get,r,r)]for r in zip(*e)]for e in d])]
