p=lambda g,k=31:-k*g or p([*zip(*[[v or(k%11)*(k%11in({*r}&{*c})|({*r[:i]}&{*r[i:]}))for*c,v,i in zip(*g,r,range(99))]for r in g])],k-1)
