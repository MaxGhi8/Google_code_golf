def p(g):
 s=sum(g,[]);n=len(g[0]);m=[[0]*n for _ in g]
 for i,k in enumerate(sorted({*s}-{0},key=lambda x:-s.count(x))):m[-1-i][i:]=[k]*(n-i)
 return m