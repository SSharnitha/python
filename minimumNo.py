n=input()
k=int(input())

i=0
ll=[]
while(i<len(n)-(k-1)):
    n1=i
    n2=i+k
    ll.append(n[n1:n2])
    i+=1

i=len(n)-k+2
while(i<len(n)+1):
    n1=i
    n2=i
    j=0
    
    while(j<(k-1)):
        n2+=1
        if(n2>len(n)):
            n2=0
        j+=1
    
    ll.append(n[n1-1:len(n)]+n[0:n2+1])
    i+=1

ll=[int(x) for x in ll]
ll.sort()
print(ll[0])
