S=sum;Z=zip;X=max
def M(m,E=enumerate):x,y=Z(*((x,y)for y,r in E(m)for x,c in E(r)if c));l,x,y=X(X(y)-min(y),X(x)-min(x))>>1,S(x)>>2,S(y)>>2;return[r[x-l:x-~l]for r in m[y-l:y-~l]]
def p(g):b=X(L:=S(g,[]),key=L.count);return[[S(v)or b for v in Z(*r)]for r in Z(*(M([[e*(e==k)for e in r]for r in g])for k in {*L}^{b}))]