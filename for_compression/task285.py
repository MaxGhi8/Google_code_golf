def p(r):
 c=len(r);m=[(2*g+1,2*i+1)for g in range(c-1)for i in range(c-1)if len({*r[g][i:i+2]+r[g+1][i:i+2]})>3]
 for i,g in[(i,g)for i in range(c)for g in range(c)if r[i][g]]:
  e,i,o,e,t=min(((u:=2*i-t)*u+(e:=2*g-o)*e,u,o,e,t)for t,o in m)
  for g,e in(-i,-e),(-i,e),(i,-e):r[t+g>>1][o+e>>1]=r[(t-1>>1)+(g>0)][(o-1>>1)+(e>0)]
 return r
