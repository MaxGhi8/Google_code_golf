p=lambda g,f=lambda x:[r for i,r in enumerate(x)if r!=x[i-1]or i<1]:[*map(list,zip(*f([*zip(*f(g))])))]
