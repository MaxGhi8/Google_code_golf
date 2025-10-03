def p(a):
 for m in range(64):
  for t in[*range(9)]*((r:=m//8)+(f:=m%8))*all(a[r+t//3][f+t%3]==(a[t//3][t%3]>0)*(m:=max(max(t[f:f+3])for t in a[r:r+3]))for t in range(9))*all(m not in t for t in a[:r]+[*zip(*a)][:f]):a[r+t//3][f+t%3]=5*(a[t//3][t%3]>0)
 return a