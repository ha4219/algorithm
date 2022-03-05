from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 999
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())
w = int(input())
a = [list(map(int, input().split())) for _ in range(w)]
d = [[MAX] * (w+1) for _ in range(w+1)]
x = [0] * (n+1)
y = [0] * (n+1)

px1 = [0] * (w+1)
py1 = [0] * (w+1)
px2 = [0] * (w+1)
py2 = [0] * (w+1)

px1[0] = py1[0] = 1
px2[0] = py2[0] = n

for i in range(w):
    px1[i+1] = a[i][0]
    py1[i+1] = a[i][1]
    px2[i+1] = a[i][0]
    py2[i+1] = a[i][1]


def dist(t, i, j):
    if t:  # p1 find
        return abs(px1[i] - px1[j]) + abs(py1[i] - py1[j])
    else:  # p2 find
        return abs(px2[i] - px2[j]) + abs(py2[i] - py2[j])


def f(i, j):
    cur = max(i, j)
    if cur == w:
        d[i][j] = 0
        return d[i][j]
    if d[i][j] != MAX:
        return d[i][j]
    d[i][j] = min(f(cur + 1, j) + dist(1, i, cur+1),
                  f(i, cur + 1) + dist(0, j, cur+1))
    return d[i][j]


def ff(i, j):
    cur = max(i, j)
    if cur == w:
        d[i][j] = 0
        return d[i][j]
    l = f(cur + 1, j) + dist(1, i, cur+1)
    r = f(i, cur + 1) + dist(0, j, cur+1)
    if l < r:
        print(1)
        ff(cur+1, j)
    else:
        print(2)
        ff(i, cur+1)
    return d[i][j]


print(f(0, 0))
# for i in d:
#     print(*i)
ff(0, 0)
