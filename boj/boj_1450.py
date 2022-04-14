import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 200000
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n, c = map(int, input().split())
a = list(map(int, input().split()))

m = n // 2
ls = [0]
rs = [0]

for i in range(m):
    for tmp in combinations(a[:m], i+1):
        ls.append(sum(tmp))

for i in range(n-m):
    for tmp in combinations(a[m:n], i+1):
        rs.append(sum(tmp))

# rs bs
rs.sort()
rsl = len(rs)
res = 0
for l in ls:
    res += bisect_right(rs, c-l)
print(res)
