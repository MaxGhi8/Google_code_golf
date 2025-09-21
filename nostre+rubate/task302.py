def p(g):
 for s in 5,4,3:
  for I in range(169):j=I%13;I//=13;M=g[I:I+s];sum(r[j:j+s].count(5)for r in M)-~-s*4 or [r.__setitem__(slice(j+1,j+~-s),[s+3]*(s-2))for r in M[1:-1]]
 return g