def p(g,R=range):
 h=len(g);w=len(g[0]);s=[(i,j)for i in R(h-1)for j in R(w-1)if g[i][j]*g[i+1][j+1]==4];f=lambda i,j:[(r,c)for r in R(i-1,i+3)for c in R(j-1,j+3)if h>r>-1<c<w and g[r][c]>7];q=f(*s[0])
 while q:
  r,c=q.pop()
  if(r,c)in f(*s[1]):return[[8]]
  g[r][c]=0
  for a,b in(1,0),(-1,0),(0,1),(0,-1):x=r+a;y=c+b;h>x>-1<y<w and g[x][y]>7and q.append((x,y))
 return[[0]]