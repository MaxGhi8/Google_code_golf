def p(p):
 for l,o,n in[(l,o,n)for l in range(len(p))for o in range(len(p[0]))for n in range(2,1+min(len(p)-l,len(p[0])-o))if all(p[l][o:o+n]+sum((p[l+e][o::~-n][:2]for e in range(n)),[])+p[l+~-n][o:o+n])]:
  for e in p[l+1:l+~-n]:e[o+1:o+~-n]=[2|n%2*5]*(n-2)
 return p