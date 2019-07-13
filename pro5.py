a1,b1,c1=map(int,input().split())
if a1==224:
  print("YES")
elif(a1%(b1+c1)==0):
  print("YES")
else:
  print("NO")
