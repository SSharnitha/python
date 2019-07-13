a1 = int(input())
b1 = list(map(int,input().split()))
c1 = 0
for i in range(a1):
    for j in range(i,a1):  
        for k in range(j,a1):
            if b1[i]<b1[j]<b1[k]:
                c1+=1
print(c1)
