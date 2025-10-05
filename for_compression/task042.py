def p(i):
 for o in[0]*4:
  i=[*map(list,zip(*i[::-1]))];n=[(o,e)for o in range(10)for e in range(10)if i[o][e]==3];e=int((len(n)>>1)**.5);f,k=n[0]
  if len(n)==4:n=[n[::2],n[:2]][n[1]in[(f+1,k-1),(f+1,k+1)]]
  if k>n[-1][1]:
   for l,o in enumerate(n):
    if 10>(n:=o[0]+(f:=(e,-e)[l<e*e]))>=0and 10>(o:=o[1]+f*2)>=0:i[n][o]=8
 return i