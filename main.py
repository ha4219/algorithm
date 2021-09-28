from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)


n = int(input())
a = [input().strip() for _ in range(n)]

def checkBit(s):
    res = 0
    for c in s:
        res |= (1<<int(c))
    return res

cnt = [0] * (1<<10)
for s in a:
    cnt[checkBit(s)]+=1

res = 0
for i in range(1<<10):
    res += (cnt[i]*(cnt[i]-1))//2
    for j in range(i+1, 1<<10):
        if (i&j)>0:
            res += cnt[i]*cnt[j]
print(res)