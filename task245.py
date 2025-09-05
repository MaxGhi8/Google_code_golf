def p(g,f=lambda g:[[v%3for v in r]for r in zip(*g)if 2in r]):
 n=[[v-v%3for v in r]for r in g];a,b=divmod(sum(g,[]).index(3),len(g[0]))
 for x in range(5):n[a+1+x][b+1:b+1+5]=f(f(g))[x]
 return n