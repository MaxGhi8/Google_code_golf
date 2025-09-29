def p(g):
 def f(s,i,d,N=0):
  if N>2or-~i>L*L or i<0:return 0
  if(s:=s[:])[i]%3<1:s[i]=3;return f(s,i+d,d,N)
  if s[i]&8:i-=d;d=[1,L][d*d<2];return f(s,i+d,d,N+1)or f(s,i-d,-d,N+1)
  return~-N*s
 s=sum(g,[]);I=s.index(3);d=[L:=len(g),1][s[I+1]&1];s=f(s,I,-d)*(s[I-d]<8)or f(s,I,d);return[*zip(*[iter(s)]*L)]