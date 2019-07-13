m1,n1=map(str,input().split())
y1=0
if len(m1)>len(n1):
	m1,n1=n1,m1
p1=0
while p1<len(m1):
	  y1+=(ord(n1[p1])-ord(m1[p1]))
	  p1+=1
for p1 in range(p1,len(n1)):
	  y1+=ord(n1[p1])-ord('a')+1
print(y1)
