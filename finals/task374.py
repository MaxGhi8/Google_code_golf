def p(g):
 for _ in g*4:l=0;g=[[[(a>0)*b|a,1<<(l:=l+1)][a%2]for a,b in zip(r,r[1:]+[0])]for*r,in zip(*g[::-1])]
 return[[[2,4,1,0][sorted({*(S:=sum(g,[]))},key=S.count).index(s)]for s in r]for r in g]