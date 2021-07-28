from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

c = 0
res = []

while n and c<100:
    if n%2:
        res.append('[/]')
        n *= 2
    elif n&2:
        res.append('[+]')
        n -= 2
    else:
        res.append('[*]')
        n //= 2
    c += 1
if n==0:
    print(c)
    res.reverse()
    print(' '.join(map(str, res)))
else:
    print(-1)