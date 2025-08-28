p=lambda g,R=range(16),A=lambda h:(h,15-h%8-8*(h//8)):[[max(g[x][y]for y in A(j)for x in A(i)if g[x][y]-4)for j in R]for i in R]
