def p(g):
 for i in range(225):c=i%15;i//=15;r=g[i];w=sum([w[c and c-1:c+2]for w in g[i and i-1:i+2]],[]).count;r[c]=(r[c]>7)*((w(4)>3-w(6))*4or w(6)and 3)or r[c]
 return g