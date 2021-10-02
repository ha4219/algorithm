from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)
MAX = 6000000
n = int(input())

k = int(input())
if k!=0:
    kill = list(map(int, input().split()))
else:
    kill = []
kills = [0] * 10
for kk in kill:
    kills[kk] = 1
k = []
for i in range(10):
    if not kills[i]:
        k.append(i)
res = abs(100-n)
for p in k:
    res = min(res, abs(p-n)+1)
    for pp in k:
        res = min(res, abs(int(str(p)+str(pp))-n)+2)
        # heappush(pq, (2, int(str(p)+str(pp))))
        for ppp in k:
            res = min(res, abs(int(str(p)+str(pp)+str(ppp))-n)+3)
            for pppp in k:
                res = min(res, abs(int(str(p)+str(pp)+str(ppp)+str(pppp))-n)+4)
                for ppppp in k:
                    res = min(res, abs(int(str(p)+str(pp)+str(ppp)+str(pppp)+str(ppppp))-n)+5)
                    for pppppp in k:
                        res = min(res, abs(int(str(p)+str(pp)+str(ppp)+str(pppp)+str(ppppp)+str(pppppp))-n)+6)
print(res)