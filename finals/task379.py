def p(g,E=enumerate):
 for i,j in[(i,j)for i,r in E(g)for j,x in E(r)if x==2]:
  for a,c in(1,0),(-1,0),(0,1),(0,-1):
    u=x=i+a;v=y=j+c
    try:
     while(x|y)<0and[][0]or g[x][y]-8:x+=a;y+=c
     while u-x|v-y:g[u][v]=2;u+=a;v+=c
     for R in g[x-1:x+2]:R[y-1:y+2]=[8]*len(R[y-1:y+2]);g[x][y]=2
    except:0
 return g