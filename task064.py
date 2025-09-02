def p(g):
 s=sum(g,[]);a,b,*_=sorted(sorted({*s}),key=s.count)
 for _ in' '*4:
  for r in(g:=[*map(list,zip(*g[::-1]))]):
    try:I=r.index;i,j=I(a),I(b);r[i:j]=[a]*(j-i)
    except:0
 return g