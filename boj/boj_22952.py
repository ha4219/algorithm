from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd
from itertools import permutations


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

# pers = list(permutations(list(range(1,n+1)), n))

# for per in pers:
#     d = [0] * (n)
#     for idx, num in enumerate(per):
#         if idx==0:
#             d[idx] = (num) % n
#         else:
#             d[idx] = (num+d[idx-1]) % n
#     s = set(d)
#     print(s)
#     if len(s)<=n//2+1:
#         print(*per)
#         print(s)
#         break

res = []
if n&1:
    for i in range(1, n//2+1):
        res.append(i)
        res.append(n-i)
    res.append(n)
else:
    for i in range(1, n//2):
        res.append(i)
        res.append(n-i)
    res.append(n)
    res.append(n//2)
print(*res)