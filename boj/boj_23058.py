from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd
from bisect import *

input = stdin.readline
setrecursionlimit(10**5)

n = int(input().strip())
a = [list(map(int, input().split())) for _ in range(n)]

res = maxsize
tot = n*n
white = 0
for i in range(n):
    for j in range(n):
        if a[i][j]:
            white += 1
black = tot - white

all_path = 2**(2*n)

for path in range(all_path):
    w, b = white, black
    for i in range(n*2):
        if path & (1<<i):
            if i>=n:
                row = i-n
                for c in range(n):
                    if path&(1<<c):
                        continue
                    elif a[c][row]:
                        w -= 1
                        b += 1
                    else:
                        w += 1
                        b -= 1
            else:
                col = i
                for r in range(n):
                    if path&(1<<(r+n)):
                        continue
                    elif a[col][r]:
                        w -= 1
                        b += 1
                    else:
                        w += 1
                        b -= 1
    cnt = 0
    for i in range(n*2):
        if path&(1<<i):
            cnt += 1
    res = min(res, min(w, b)+cnt)
print(res)
