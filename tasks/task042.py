def p(g,E=range(10)):
 for _ in' '*4:
  g=[*map(list,zip(*g[::-1]))];S=[(r,c)for r in E for c in E if g[r][c]==3];m=int((len(S)>>1)**.5);a,b=S[0]
  if len(S)==4:S=[S[::2],S[:2]][S[1]in[(a+1,b-1),(a+1,b+1)]]
  if b>S[-1][1]:
   for i,C in enumerate(S):
    if-1<(x:=C[0]+(a:=(m,-m)[i<m*m]))<10>(y:=C[1]+a*2)>=0:g[x][y]=8
 return g