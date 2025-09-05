def p(g,f=lambda g:[[v%3for v in r]for r in zip(*g)if 2in r]):
 n=[[v-v%3for v in r]for r in g];t=sum(g,[]).index(3);w=len(g[0])
 for x in range(5):n[t//w+1+x][t%w+1:t%w+6]=f(f(g))[x]
 return n