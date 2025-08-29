def p(g):
 for A in range(441):a=A//7//9;b=A%63//9;i=A%9//3;j=A%3;g[x][y]=g[x:=a+i][y:=b+j]or(4in{*[*zip(*g)][y][a:a+3]}&{*g[x][b:b+3]})*7
 return g