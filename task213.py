def p(g):
 if t:=len({*(g[0]+g[-1])})>3:g=[*zip(*g)]
 m=[[({*r}-{0,5}).pop()]for r in g if{*r,0,5}>{0,5}];m=[r*len(m)for r in m];return[*zip(*m)]if t else m