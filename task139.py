def p(g):
 for A in range(441):a=A//63;b=A//9%7;g[x][y]=g[x:=a+A//3%3][y:=b+A%3]or(4in{*[*zip(*g)][y][a:a+3]}&{*g[x][b:b+3]})*7
 return g