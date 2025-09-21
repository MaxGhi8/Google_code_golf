def p(g):
 w=len(g[0]);h=len(g)
 def f(i,j):
  g[i][j]=3
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   try:g[x:=i+x][y:=j+y]<1and f(x,y)
   except:0
 for I in range(h*w):g[i:=I//w][j:=I%w]<1and i*(h+~i)*j*(w+~j)<1and f(i,j)
 return[[c or 2for c in r]for r in g]