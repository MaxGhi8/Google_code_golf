p=lambda g:[[a or b or c or d for a,b,c,d in zip(x,x[5:],y,y[5:])]for x,y in zip(g,g[5:])]
