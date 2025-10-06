import re
def p(i):
 r=re.sub(', ','',str(i+[*zip(*i)]));i=int(max(r,key=r.count));l={0:(0,i)}
 for t in range(10):
  if(t!=i)*(e:=re.findall(f'{t}+',r+r[::-1])):d=len((re.findall(f'{t}{t}([^]){t}]+){t}|$',r+r[::-1]))[0]);l[len(max(e))*((d>0)+1)+d>>1]=d+1>>1,t
 return[[i*((d:=l[r[1]])[0]>r[0])or d[1]for t in range(-max(l),max(l)+1)if(r:=sorted((abs(t),abs(e))))]for e in range(-max(l),max(l)+1)]