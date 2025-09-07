def p(g,r=range):
 h=[0]*18
 for i in r(18):
  for j in r(w:=0,18):
   if(n:=g[i][j]<1)&w&h[j]&~((j>2==g[i][j-2]<i)&(g[i-2][j-2:j]==[2,2])):
    for y in(i-1,i):g[y][j-1:j+1]=2*[2]
   h[j],w=n*w,n
 return g
