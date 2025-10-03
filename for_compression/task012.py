def p(r):
 e=[e[:]for e in r];i,g=sorted({*(f:=sum(r,[]))},key=f.count)[:2]
 for n in range(2500):s,k=n//250,n//25%10;n%=25;e[s+n//5-2][k+n%5-2]|=(n in{2,10,14,22})*g*(f:=r[s][k]==i)or(n%2<1)*i*f
 return e