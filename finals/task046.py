def p(g):
 L=[];l=[]
 for c in zip(*g):
  if sum(c):l+=c,
  else:L+=l,;l=[]
 if l:L+=l,
 for a,b in zip(L,L[1:]):
  s=(b[0].index(5)-a[-1].index(5))%3;b[:]=[r[s:]+r[:s]for r in b]
 return[sum(x,[])for x in zip(*[[[*map({5:max({*sum(l,())}-{0,5})}.get,r,r)]for r in zip(*l)]for l in L])]