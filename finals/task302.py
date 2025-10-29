p=lambda g,k=3:-k*g or p([r.count(5)>1and((i:=r.index(5)),(d:=r[i+1:].index(5)),r[:i+1]+(d+5,)*d+r[i-~d:])[-1]or r for r in zip(*g[::-1])],k-1)
