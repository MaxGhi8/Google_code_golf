def p(g,E=enumerate,f=lambda g:[[*r]for r in zip(*g)if any(r)],s=lambda g:divmod(sum(g,[]).index(8),len(g[0]))):
 a,b=s(g);A,B=s(G:=f(f(g)));M=[len(g[0])*[0]for _ in[0]*len(g)]
 for h,R in E(G):
  for k,V in E(R):M[a-A+h][b-B+k]=V
 return M