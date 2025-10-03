def p(q):
 def j(n,r):
  q[n][r]=3;l=1+sum(j(n,r)for n,r in((n+1,r),(n-1,r),(n,r+1),(n,r-1))if 0<=n<10>r>=0<q[n][r]//5);q[n][r]=5;return l
 return[[q[n][r]and[2,4,1][sum(f<j(n,r)for f in{j(n,r)for n in range(10)for r in range(10)if q[n][r]})]for r in range(10)]for n in range(10)]