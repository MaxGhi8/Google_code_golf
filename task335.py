def p(g,E=enumerate):
 d={k:(i,j)for i,r in E(g)for j,k in E(r)};l,y,k,W=d[2]+d[8]
 for r in g[k+1:l+1]or g[l:k]:r[W]=4
 g[l][W:y:y>W or-1]=[4]*abs(y-W);return g