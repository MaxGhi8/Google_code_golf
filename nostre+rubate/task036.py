def p(g,S=sorted):
 d={}
 for i in range(900):
  if x:=g[i//30][i%30]:s=d.setdefault(x,[set(),set()]);s[0]|={i//30};s[1]|={i%30}
 u,v=d[min(((max(R)-min(R)+1)*(max(C)-min(C)+1),k)for k,(R,C)in d.items())[1]];return[[g[i][j] for j in S(v)]for i in S(u)]