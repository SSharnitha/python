n2=int(input())
l2=list(map(int,input().split()))
c2=0
for i in range(0,n2):
    for j in range(0,i):
        if l2[j]<l1[i]:
            c2=c2+l2[j]
print(c2)
