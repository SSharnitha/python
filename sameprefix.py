n=int(input())
st=[]
for i in range(0,n):
    s=input()
    st.append(s)

i=0
count=0
f=True
for i in range(0,len(st[0])):
    if(f==False):
        break
    j=1
    while(j<n and st[0][i]==st[j][i]):
        j+=1
    if(j==n):
        count+=1
    else:
        f=False
        break
    
for i in range(0,count):
    print(st[0][i],end="")
