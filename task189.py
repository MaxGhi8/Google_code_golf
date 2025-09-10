def p(g,k=0,a=range(3,9)):
 if g[0][2]*g[2][0]==64:g=[[g[r>5][c>5]*(g[r][c]>0)for c in a]for r in a]
 return(k>3)*g or p([*zip(*g[::-1])],k+1)