def p(g,R=range):
 h,w,k=len(g),len(g[0]),0
 def f(i,j):
  g[i][j]=0
  for x,y in(1,0),(-1,0),(0,1),(0,-1):
   if h>(x:=i+x)>-1<(y:=j+y)<w and g[x][y]:f(x,y)
 for i in R(h*w):
  if g[i//w][i%w]:k+=1;f(i//w,i%w)
 return[[8*(i==j)for j in R(k)]for i in R(k)]