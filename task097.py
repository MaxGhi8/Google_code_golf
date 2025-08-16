p=lambda g,E=enumerate:[[0 if g[i][j]>0 and all((x==y==0 or not(0<=i+x<len(g)and 0<=j+y<len(r)and g[i+x][j+y]>0))for x in(-1,0,1)for y in(-1,0,1))else g[i][j]for j,c in E(r)]for i,r in E(g)]
