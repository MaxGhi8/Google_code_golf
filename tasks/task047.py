def p(g,R=range(9)):
 L=[(v,i,j)for i in R for j in R if(v:=g[i][j])]
 for(v,i,j)in L:
  for x in R:g[i][x]=g[x][j]=v
 (_,a,b),(_,c,d)=L;g[a][d]=g[c][b]=2;return g