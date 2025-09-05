def p(g,R=range):
 z=max(z+21for z in R(274)if(f:=sum(g,[]))[z]==5==f[z+126]);l=max(t:=sum(s:=[r[z%20:][:5]for r in g[z//20:][:5]],[]))
 for i in R(256):
  y=i>>4;x=i&15
  for a in[*R(5)]*all(g[y+a//5][x+a%5]*l==t[a]for a in R(25)):g[y+a][x:x+5]=s[a]
 return g