s=input()
s=list(s)
s1=""
n1=len(s)-1
for i in range(0,len(s)//2+1):
    temp=s[i]
    s[i]=s[n1-i]
    s[n1-i]=temp
s1=s1.join(s)
print(s1)
