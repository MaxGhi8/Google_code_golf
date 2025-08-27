def p(g):
 m=[p[:]for p in g];k,h=sorted({*(s:=sum(g,[]))},key=s.count)[:2]
 for t in range(2500):r,c,I=t//250,t//25%10,t%25;m[r+I//5-2][c+I%5-2]|=(I in{2,10,14,22})*h*(v:=g[r][c]==k)or(I%2<1)*k*v
 return m