def p(g,K=0):
 for r in g:K=[K,k:=max(r)][k>0];j=r.index(k);r[j:]=[k]*len(r[j:]);r[-1]=K
 return g