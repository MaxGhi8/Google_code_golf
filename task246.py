def p(g,E=enumerate):
 L=[(v,i,j)for i,r in E(g)for j,v in E(r)];L.sort();_,C,A,_,D,B=L[-2]+L[-1];R,V=[[A+1,B+1],[B,A]][A>B];g[C][R:V]=[8]*(V-R);K,W=[[D+1,C],[C+1,D]][C<D]
 for R in g[K:W]:R[B]=8
 return g