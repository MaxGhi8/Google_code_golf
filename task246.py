def p(g,E=enumerate):
 (_,C,A),(_,D,B)=sorted((v,i,j)for i,r in E(g)for j,v in E(r))[-2:];R,V=[[A+1,B+1],[B,A]][A>B];g[C][R:V]=[8]*(V-R)
 for R in g[min(D+1,C):max(C+1,D)]:R[B]=8
 return g