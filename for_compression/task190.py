def p(f):
 for i in 0,1:r=sum(f:=f[::-1],[]);i=min(i for i in range(100)if r[i]*r[i-1]);n=i//10;d=i-1;f[:n]=[[max(r)*((o==n+i%10-f)*(r[i-9]>0)+(o==d//10+f-d%10)*(r[i-12]>0))for f in range(10)]for o in range(n)]
 return f
