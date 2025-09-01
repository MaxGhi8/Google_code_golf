def p(g,R=range):
 z=[z+21for z in R(274)if(f:=sum(g,[]))[z]==5==f[z+126]][~0];l=max(sum(s:=[r[z%20:][:5]for r in g[z//20:][:5]],[]))
 for i in R(256):
  if all(g[i//16+a//5][i%16+a%5]==s[a//5][a%5]//l for a in R(25)):
   for a in R(25):g[i//16+a//5][i%16+a%5]=s[a//5][a%5]
 return g