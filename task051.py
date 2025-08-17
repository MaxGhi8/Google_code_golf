def p(g,k=4):
 g=[(r[:j]+[k or v for k in r[j:]]if 1>r[j-1]<len({*r[j-1:j+2]})>2 else r)[j]for r in g for j,v in enumerate(r)]
 return p([*map(list,zip(*g[::-1]))],k-1)if k else g