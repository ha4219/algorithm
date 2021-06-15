from sys import stdin, setrecursionlimit, maxsize
from collections import deque


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = [sorted(input().strip()) for _ in range(n)]
a.sort()
res = 1

for i in range(n-1):
    if a[i]==a[i+1]:
        continue
    res += 1
print(res)

