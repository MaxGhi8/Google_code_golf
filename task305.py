def p(g):
 k=len({*sum(g,[])}-{0})
 for _ in [0]*9:g=[[r[j]or(j+k<16)*r[(j+k)%16]or(j>k-1)*r[j-k]for j in range(16)]for r in g]
 return g