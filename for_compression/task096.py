import re
def p(p):
 o=re.sub(r',\s','',str(p+[*zip(*p)]));o+=o[::-1];i=int(max(o,key=o.count));s={0:(0,i)}
 for j in{*range(10)}-{i}:
  if(t:=re.findall(f'{j}+',o)):
   n=len((re.findall(f'{j}{j}[^]){j}]+{j}',o)+[3*'0'])[0])-3
   t=len(max(t,key=len))*(1,2)[n>0]
   s[(t+n)//2]=((n+1)//2,j)
 r=2*max(s)+1
 return[[i if(t[0]<(t:=s[t[1]])[0])else t[1]for j in range(r)if(t:=sorted([abs(j-r//2),abs(e-r//2)]))]for e in range(r)]