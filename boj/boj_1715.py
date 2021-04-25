from sys import stdin
from heapq import *


input = stdin.readline
pq = []

for _ in range(int(input())):
    heappush(pq, int(input()))

res = 0
while len(pq)>1:
    a,b=heappop(pq),heappop(pq)
    t = a+b
    heappush(pq, t)
    res += t
print(res)