from itertools import combinations
m1,k1=map(int,input().split())
a1=len(str(m1))
lst1=list(combinations(str(m1),a1-k1))
lst1=sorted(lst1)
print(*lst1[0],sep='')
