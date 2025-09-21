def p(g):
 w=len(g[0]);h=len(g);l=min(i for r in g if r.count(0)>9 for i in range(w)if r[i])+1
 def f(i,j):
  g[i][j]=4
  for a,b in(1,0),(-1,0),(0,1),(0,-1):h>(x:=i+a)>-1<(y:=j+b)<w and g[x][y]<1 and f(x,y)
 for I in range(h*w):g[i:=I//w][j:=I%w]<1and(-~i%l<1and i or -~j%l<1and j)and f(i,j)
 return[[c or 3for c in r]for r in g]