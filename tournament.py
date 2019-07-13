    
p1=int(input())
q1=[]
r1=0
for i in range (0,p1+1):
    r1=abs((2**i)-p1)
    q1.append(r1)
print(min(q1))
