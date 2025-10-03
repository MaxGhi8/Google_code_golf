def p(z,l=lambda z:[l for*l,in zip(*z)if sum(l)],n=lambda z:divmod(sum(z,[]).index(8),len(z[0]))):
 b,m=n(z);o,l=n(n:=l(l(z)));y=[[0]*len(z[0])for p in z]
 for t,n in enumerate(n):
  for s,n in enumerate(n):y[b-o+t][m-l+s]=n
 return y
