a,s=input().split()
s1=abs(len(s)-len(a))
for i in range(len(a)):
  if(len(s)==1 and s[i] in a):
    break
  if(a[i]!=s[i]):
    s1=s1+1
print(s1)
