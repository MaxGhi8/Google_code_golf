import re
def p(g,R=range,f=re.findall):
 t=re.sub(r',\s','',str(g+[*zip(*g)]));t+=t[::-1];b=int(max(t,key=t.count));B={0:(0,b)}
 for c in{*R(10)}-{b}:
  if(v:=f(f'{c}+',t)):
   m=len((f(f'{c}{c}[^]){c}]+{c}',t)+[3*'0'])[0])-3
   l=len(max(v,key=len))*(1,2)[m>0]
   B[(l+m)//2]=((m+1)//2,c)
 x=2*max(B)+1
 return[[b if(z[0]<(p:=B[z[1]])[0])else p[1]for j in R(x)if(z:=sorted([abs(j-x//2),abs(i-x//2)]))]for i in R(x)]