def p(g):
 D,K,*d={},sorted(range(10),key=sum(g,[]).count),
 for i,r in enumerate(g):
  for j,c in enumerate(zip(*g)):
   if(v:=g[i][j])in(C:={*K[-4:-2]}):
    d+=i+j,i-j+.1
    if len(e:={*r}-{v})<2and r.count(v)<3or len(e:={*c}-{v})<2and c.count(v)<3:
     D[k:=e.pop()]=v;D[({*K[-2:]}-{k}).pop()]=(C-{v}).pop()
 return[[[D.get(v,v),v][not{i+j,i-j+.1}&{*d}]for j,v in enumerate(r)]for i,r in enumerate(g)]