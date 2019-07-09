def pat(s):
    res=""
    i=0
    count=0
    while(i<len(s)):
        res=res+str(count)
        count=0
        ch=s[i]
        while i<len(s) and s[i]==ch:
            count+=1
            i+=1
        count+=1
    return res

s=input()
s=s.split()
s1=list(s[0])
s2=list(s[1])
n1=pat(s1)
n2=pat(s2)
if n1==n2:
    print("yes")
else:
    print("no")

