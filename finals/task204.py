def p(g):
 R=range;h,w=len(g),len(g[0])
 for i,j,l in[(i,j,l)for i in R(h)for j in R(w)for l in R(2,1+min(h-i,w-j))if all(g[i][j:j+l]+sum((g[i+k][j::~-l][:2]for k in R(l)),[])+g[i+~-l][j:j+l])]:
  for r in g[i+1:i+~-l]:r[j+1:j+~-l]=[2|l%2*5]*(l-2)
 return g