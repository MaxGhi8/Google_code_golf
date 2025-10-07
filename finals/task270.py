import re
def p(g):
 for k,K in zip('21','37'):
  for _ in' '*4:g=[[*map(int,re.sub(k+'(.)(.*?)'+K,k+K+r'\2\1',str(w)[1::3]))]for*w,in zip(*g[::-1])]
 return g