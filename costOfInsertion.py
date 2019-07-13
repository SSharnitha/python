d,a=map(s,input().split())
e1=0
if len(d)>len(a):
   d,a=a,d
r1=0
while r1<len(d):
   e1+=(ord(a[r])-ord(d[r]))
   r1+=1
for r1 in range(r1,len(a)):
   e1+=ord(a[r])-ord('a')+1
print(e1)
