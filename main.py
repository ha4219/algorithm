from sys import stdin
from heapq import *


n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

a.sort(key=lambda x:x[0])
res = 1
pq = []
first = True
for i in range(n):
    if first:
        first = False
        heappush(pq,a[i][1])
    else:
        e=heappop(pq)
        if e<=a[i][0]:
            heappush(pq,a[i][1])
        else:
            heappush(pq,e)
            heappush(pq,a[i][1])
print(len(pq))