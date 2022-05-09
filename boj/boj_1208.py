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

ls = []
rs = []

res = 0


def l(i, s):
    if i >= n//2:
        return
    s += a[i]
    if s == c:
        global res
        res += 1
    ls.append(s)
    l(i+1, s-a[i])
    l(i+1, s)
    return


def r(i, s):
    if i >= n:
        return
    s += a[i]
    if s == c:
        global res
        res += 1
    rs.append(s)
    r(i+1, s-a[i])
    r(i+1, s)
    return


l(0, 0)
r(n//2, 0)
# rs bs
rs.sort()
for i in ls:
    left = bisect_left(rs, c-i)
    right = bisect_right(rs, c-i)
    res += right - left

print(res)
