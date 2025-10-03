def p(n):
 d=min(i for d in n if d.count(0)>9 for i in range(len(n[0]))if d[i])+1
 def p(i,f):
  n[i][f]=4
  for k,d in(1,0),(-1,0),(0,1),(0,-1):len(n)>(e:=i+k)>-1<(l:=f+d)<len(n[0])and n[e][l]<1 and p(e,l)
 for m in range(len(n)*len(n[0])):n[i:=m//len(n[0])][f:=m%len(n[0])]<1and(-~i%d<1and i or -~f%d<1and f)and p(i,f)
 return[[e or 3for e in d]for d in n]