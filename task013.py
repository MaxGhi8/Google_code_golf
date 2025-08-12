def p(g,E=enumerate):
 L=[(v,i,j)for i,r in E(g)for j,v in E(r)];L.sort();a,b,c,d,e,f=L[-2]+L[-1];n=len(g[0])
 if c*f in[0,(n-1)**2]:D=abs(b-e)*2;g[b::D],g[e::D]=[[a]*n]*len(g[b::D]),[[d]*n]*len(g[e::D]);return g
 for r in g:D=abs(c-f)*2;r[c::D]=[a]*len(r[c::D]);r[f::D]=[d]*len(r[f::D])
 return g