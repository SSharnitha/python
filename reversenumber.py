s=int(input())
s=list(str(s))
s1=""
n=len(s)
n1=n-1
if(n%2==0):
    n=len(s)//2
else:
    n=len(s)//2+1
for i in range(0,n):
    temp=s[i]
    s[i]=s[n1-i]
    s[n1-i]=temp
s1=s1.join(s)
print(int(s1))
