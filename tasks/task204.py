import re;p=lambda g,k=3:-k*g or p([eval(re.sub('1, (([^1], )*)1',lambda m:'1,'+f'{2+5*(len(m[1])%2)},'*(len(m[1])//3)+'1'if m[1]else m[0],str(r),count=1))for r in zip(*g[::-1])],k-1)
