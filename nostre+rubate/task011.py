def p(j,R=range):
 *k,=map(list,j)
 for d in R(9):
  for v in R(81*(sum(j[d//3*4+W][d%3*4+l]<1for W in R(3)for l in R(3))>4)):k[v%3*4+v//9%3][v//3%3*4+v//27]=j[d//3*4+v%3][d%3*4+v//3%3]
 return k