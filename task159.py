def p(g,f=lambda g,k:[[*r]for r in zip(*g)if k in r]):
 k=sum({*sum(g,[])})-2;l=len(n:=f(f(g,2),2))-2;t=l//3
 for x in range(l*l):n[x//l+1][x%l+1]=f(f(g,k),k)[x//l//t][x%l//t]
 return n