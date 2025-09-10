def p(g):
 s=sum(g,[]);v,k=[*{x for x in s if x}]
 if[k,k]!=s[s.index(k)+19:][:2]:x=v;v=k;k=x
 for I in range(400):
  for a in(g[i:=I//20][j:=I%20]==k)*[*range(i,20)]*(v in[*zip(*g[i:])][j]):g[a][j]=g[a][j]or v
 return g