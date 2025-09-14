def p(g,e=enumerate):
 (r,c,A),(R,C,B)=[(i,j,x)for i,r in e(g)for j,x in e(r)if x];f=c==C
 if f:g=[*map(list,zip(*g))];r,c,R,C=c,r,C,R
 if c>C:r,c,A,R,C,B=R,C,B,r,c,A
 d=C-c-1>>1
 for r,c,W,S in(r,c,A,1),(R,C,B,-1):
  g[r][c:c+S*d:S]=[W]*d;j=c+S*d-S
  for k in-2,-1,1,2:u=g[r+k];u[j+S*(~k&1)]=u[j]=W
 return[*zip(*g)]*f or g