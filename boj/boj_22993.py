from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int, input().split()))

pq = []
for i in a[1:]:
    heappush(pq, i)
x = a[0]
while pq:
    y = heappop(pq)
    if x>y:
        x += y
    else:
        heappush(pq, y)
        break
print('No' if len(pq) else 'Yes')