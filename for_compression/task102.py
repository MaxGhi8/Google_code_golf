def p(a):
 for d in range(121):
  t=d%11;d//=11
  for f in range(12-d):
   n=a[d:d+f];e=t+f
   if all(a[d-1][t:e]+a[d+f][t:e]+[l[e:]and l[t-1]&l[e]and 5not in l[t:e]for l in n]):
    for l in n:l[t:e]=[2]*f
 return a