def p(g):
 A=[]
 for v in sum(g,[]):A+=[v]*(v not in A)
 return [[A],[[x]for x in A]][A[0]==g[0][-1]]