def p(g):
 k=(s:=sum(g,[])).index(2)
 for i in range(10-max(k%10,k//10)):s[k+11*i]=2
 k=s.index(1)
 for i in range(min(k%10,k//10)+1):s[k-11*i]=1
 return[*zip(*[iter(s)]*10)]