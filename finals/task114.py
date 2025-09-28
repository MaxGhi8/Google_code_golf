def p(g):
 g=[R[:1]+R+R[-1:]for R in g[:1]+g+g[-1:]]
 for r in g[0],g[-1]:r[0]=r[-1]=0
 return g