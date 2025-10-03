def p(g):
 for _ in[0]*4:
  g=[*zip(*g)][::-1];L=[]
  for i,r in enumerate(g):2in r and(L.append(r),b:=i);8in r and(a:=i)
  a<b and 2not in g[a]and(g:=(g[:a+1]+L+[[0]*len(r)]*99)[:len(g)])
 return g