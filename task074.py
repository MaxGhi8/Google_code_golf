p=lambda g:[g:=[[*map(lambda X:max(x%9for x in X),zip(*r,[0,0]+r[0][::-1]))]for r in zip(g,zip(*g))]for _ in" "*3][2]
