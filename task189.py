def p(g,k=0,R=range(3,9)):
 if g[0][2]*g[2][0]==64:g=[[g[(r-2)//4][(c-2)//4]*(g[r][c]>0)for c in R]for r in R]
 return(k>3)*g or p([*map(list,zip(*g[::-1]))],k+1)