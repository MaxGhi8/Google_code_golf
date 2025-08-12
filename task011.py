def p(j,A=range(3)):
 k=[r[:] for r in j]
 for d in range(9):
  for v in range(81*(sum(j[d//3*4+W][d%3*4+l]<1for W in A for l in A)>4)):k[v%3*4+v//9%3][v//3%3*4+v//27]=j[d//3*4+v%3][d%3*4+v//3%3]
 return k