import math
p2,q2=map(int,input().split())
r2=[]
s2=list(map(int,input().split()))
for i in range(0,q2):
    u2,v2=map(int,input().split())
    r2.append([u2,v2])
for i in r2:
    x2=i[0]-1
    y2=i[1]-1
    print(math.gcd(s2[x2],s2[y2]))
