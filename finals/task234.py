def p(g,k=0,e=enumerate):
 *g,=map(list,zip(*g[::-1]));L=[i for i,r in e(g)if r.count(next(filter(None,sum(g,[]))))==1]
 if L:l,m=L[0],len(L);g=[[0]*len(g[0])]*m+g[:l]+g[l+m:]
 return k<3 and p(g,k+1)or g