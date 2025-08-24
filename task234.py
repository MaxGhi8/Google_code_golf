def p(g,K=0,E=enumerate):
 g=[*map(list,zip(*g[::-1]))];L=[i for i,r in E(g)if r.count([*filter(None,sum(g,[]))][0])==1]
 if L:l,m=L[0],len(L);g=[[0]*len(g[0])for _ in[0]*m]+g[:l]+g[l+m:]
 return g if K>2 else p(g,K+1)