def p(g):
 m,r,*d={},sorted(range(10),key=sum(g,[]).count),
 for o,n in enumerate(g):
  for a,c in enumerate(zip(*g)):
   if(e:=g[o][a])in(q:={*r[-4:-2]}):
    d+=o+a,o-a+.1
    if len(h:={*n}-{e})<2and n.count(e)<3or len(h:={*c}-{e})<2and c.count(e)<3:
     m[k:=h.pop()]=e;m[({*r[-2:]}-{k}).pop()]=(q-{e}).pop()
 return[[[m.get(e,e),e][not{o+a,o-a+.1}&{*d}]for a,e in enumerate(n)]for o,n in enumerate(g)]