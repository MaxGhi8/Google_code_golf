def p(m):
 def f(g,r,m):
  e=1
  for l,o in(1,0),(-1,0),(0,1),(0,-1):
   if 10>(l:=g+l)>-1<(o:=r+o)<10 and m[l][o]>4:m[l][o]=-1;e+=f(l,o,m)
  return e
 return[[m[g][r]and(f(g,r,[*map(list,m)])==7)+1for r in range(10)]for g in range(10)]