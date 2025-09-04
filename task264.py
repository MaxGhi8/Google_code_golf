def p(g,R=range):
 w=len(g[0]);m=[[5]*9for _ in R(9)]
 for q in[q for z in R(w*len(g))if(0not in(q:=sum((r[z%w:][:3]for r in g[z//w:][:3]),[])))*q[8:]]:
  for a in(k:={*q}-{5})and R(3):v=q[4]!=5;o=2*q[v::2].index(*k)+v;m[o-o%3+a][o%3*3:o%3*3+3]=q[a*3:][:3]
 return m