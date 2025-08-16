def p(g,E=enumerate):d=[[sum(g[a+i][b+j]for a,r in E(g)for b,v in E(r)if v==5)for j in(-1,0,1)]for i in(-1,0,1)];d[1][1]=5;return d
