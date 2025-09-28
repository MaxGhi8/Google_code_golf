f=lambda g:g*all(map(any,g))or f([*zip(*filter(any,g))])
p=lambda g:f([[x*(x==min({*(s:=sum(g,[]))}-{0},key=s.count))for x in r]for r in g])