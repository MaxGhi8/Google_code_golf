def p(g,R=range):
 for _ in 0,1:s=sum(g:=g[::-1],[]);a=min(i for i in R(100)if s[i]*s[i-1]);q=a//10;t=a-1;g[:q]=[[max(s)*((r==q+a%10-c)*(s[a-9]>0)+(r==t//10+c-t%10)*(s[a-12]>0))for c in R(10)]for r in R(q)]
 return g