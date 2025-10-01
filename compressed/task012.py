def p(r):
 o=[f[:]for f in r];a,s=sorted({*(e:=sum(r,[]))},key=e.count)[:2]
 for e in range(2500):f,n=e//250,e//25%10;e%=25;o[f+e//5-2][n+e%5-2]|=(e in{2,10,14,22})*s*(n:=r[f][n]==a)or(e%2<1)*a*n
 return o