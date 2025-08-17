def p(m):k=sum(r.count(5)for r in m);m=[[x*(x!=5) for x in r]for r in m];return [r[k:]+r[:k]for r in m[-k:]+m[:-k]]
