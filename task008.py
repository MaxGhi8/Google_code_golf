def p(g,e=enumerate,f=lambda g:[[*r]for r in zip(*g)if any(r)],s=lambda g:divmod(sum(g,[]).index(8),len(g[0]))):
 a,b=s(g);A,B=s(G:=f(f(g)));M=[[0]*len(g[0])for _ in g]
 for h,R in e(G):
  for k,v in e(R):M[a-A+h][b-B+k]=v
 return M