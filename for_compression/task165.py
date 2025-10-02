def p(g):
 s=sum(g,[]);v,k={*s}-{0}
 if[k,k]!=s[s.index(k)+19:][:2]:v,k=k,v
 for I in range(400):
  for a in(g[i:=I//20][j:=I%20]==k)*[*range(i,20)]*(v in[*zip(*g[i:])][j]):g[a][j]=g[a][j]or v
 return g