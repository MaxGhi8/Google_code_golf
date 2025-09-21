def p(g,R=range):
 for _ in R(3):n=len(g[0]);g=[[g[i][j]or g[(i+10)%20][j]or g[i][(j+10)%(n//9*10)]for j in R(n)]for i in R(19)]
 return g