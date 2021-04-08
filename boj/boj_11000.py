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
        if pq[0]<=a[i][0]:
            heappush(pq,a[i][1])
        else:
            heappop(pq)
            heappush(pq,a[i][1])
print(len(pq))