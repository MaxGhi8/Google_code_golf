def p(r):
 h=len(r);h=len(r[0]);m=[(2*b+1,2*i+1)for b in range(h-1)for i in range(h-1)if len({*r[b][i:i+2]+r[b+1][i:i+2]})>3]
 for i,b in[(i,b)for i in range(h)for b in range(h)if r[i][b]]:
  _,i,d,e,t=min(((u:=2*i-t)*u+(e:=2*b-d)*e,u,d,e,t)for t,d in m)
  for b,e in(-i,-e),(-i,e),(i,-e):r[t+b>>1][d+e>>1]=r[(t-1>>1)+(b>0)][(d-1>>1)+(e>0)]
 return r