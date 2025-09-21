p=lambda g,R=range:[[g[i%((s:=min((sum(map(max,zip(*([0]*s*k+sum(g,[])+[0]*99for k in R(9))))),s)for s in R(1,40))[1])//10)][J:=j-s%10*(i//(s//10))]*(J>=0)for j in R(10)]for i in R(10)]
