from itertools import combinations
m,k=map(int,input().split())
a=len(str(m))
lst=list(combinations(str(m),a-k))
lst=sorted(lst)
print(*lst[0],sep='')
