def p(g):
 s=sum(g,[]);n=len(g[0]);m=[[0]*n for _ in g]
 for i,k in enumerate(sorted({*s}-{0},key=s.count)[::-1]):m[~i][i:]=[k]*(n-i)
 return m