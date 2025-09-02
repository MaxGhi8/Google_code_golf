L=len
R=range
E=enumerate
def M(m,C):return sorted([[y,x] for y,r in E(m) for x,c in E(r) if c==C])
def p(g):
 h,w=L(g),L(g[0])
 X=[r[:] for r in g]
 P=sorted([[sum(g,[]).count(C),C] for C in R(9)])
 d={k:M(g,k) for v,k in P[:-2]}
 Z=M(g,P[-2][1])
 h,w=L(g),L(g[0])
 for C in d:
  if L(d[C])>0:
   for m in range(1,10):
    r,c=d[C][0][0]-Z[0][0],d[C][0][1]-Z[0][1]
    if r<0: r+=-1 #extremety points need more work
    r*=m
    c*=m
    for y,x in Z:
     if r+y>=0 and c+x>=0:
      try:
       X[r+y][c+x]=C
      except: pass
 return X
