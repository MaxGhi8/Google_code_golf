def p(g,E=enumerate):d=[[sum(g[a+i-1][b+j-1]for a,r in E(g)for b,v in E(r)if v==5)for j in(0,1,2)]for i in(0,1,2)];d[1][1]=5;return d
