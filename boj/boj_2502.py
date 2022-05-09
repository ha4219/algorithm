import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 200000
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

d = [[0, 0] for _ in range(31)]
d[0] = [0, 0]
d[1] = [1, 0]
d[2] = [0, 1]
for i in range(3, 31):
    d[i][0] = d[i-1][0] + d[i-2][0]
    d[i][1] = d[i-1][1] + d[i-2][1]

day, k = map(int, input().split())

p, q = d[day]
for i in range(1, k+1):
    tk = k - p*i
    if tk % q == 0:
        a = i
        b = tk//q
        break
print(a)
print(b)
