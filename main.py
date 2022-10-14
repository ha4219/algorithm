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

n = int(input())

sx, sy, ex, ey = map(int, input().split())

res = maxsize
ret = -1

for i in range(n):
    px, py = sx, sy
    tmp = 0
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        tmp += abs(px - x) + abs(py - y)
        px, py = x, y
    tmp += abs(px - ex) + abs(py - ey)
    if tmp < res:
        res = tmp
        ret = i + 1
print(ret)
