w,w1=map(str,input().split())
x1=0
if len(w)>len(w1):
   w,w1=w1,w
s1=0
while s1<len(w):
   x1+=(ord(w[s1])-ord(w[s1]))
   s1+=1
for s1 in range(s1,len(w1)):
   x1+=ord(w1[s1])-ord('a')+1
print(x1)
