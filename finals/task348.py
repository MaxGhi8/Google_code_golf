def p(g):
 h=sum(7 in r for r in g);c=g[0].index(7)
 for i in range(h):
  for x in range(max(0,c-h+1+i),min(len(g[i]),c+h-i)):g[i][x]=7+(x+c)%2
 return g