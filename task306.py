def p(g):
 for _ in [0]*3:n=len(g[0]);g=[[g[i][j]or g[(i+10)%20][j]or g[i][(j+10)%(n//9*10)]for j in range(n)]for i in range(19)]
 return g