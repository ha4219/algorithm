from sys import stdin
from heapq import *


input = stdin.readline
MOD = 10**9+7

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    pq = []
    res = 1
    for i in a:
        heappush(pq, i)
    while len(pq)!=1:
        x,y = heappop(pq),heappop(pq)
        r = (x * y) % MOD
        res *= r
        res %= MOD
        heappush(pq, x*y)
    print(res)