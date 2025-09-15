def p(g,R=range(10)):
 f=lambda i,j,m:1+sum(m[a].__setitem__(b,-1)or f(a,b,m)for x,y in zip((1,-1,0,0),(0,0,1,-1))if 10>(a:=i+x)>-1<(b:=j+y)<10and m[a][b]>4)
 return[[g[i][j]and 6-f(i,j,[*map(list,g)])for j in R]for i in R]