def prime(n):
    i=2
    while(i<n):
        if n%i==0:
            return False
        i+=1
    return(True)

n=input()
n=n.split()
i=int(n[0])
j=int(n[1])
count=0
while(i<=j):
    if(prime(i)):
        count+=1
    i+=1
print(count)
