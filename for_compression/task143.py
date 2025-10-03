def p(g):
 for t in range(64):
  for a in[*range(9)]*((i:=t//8)+(j:=t%8))*all(g[i+a//3][j+a%3]==(g[a//3][a%3]>0)*(m:=max(max(r[j:j+3])for r in g[i:i+3]))for a in range(9))*all(m not in x for x in g[:i]+[*zip(*g)][:j]):g[i+a//3][j+a%3]=5*(g[a//3][a%3]>0)
 return g