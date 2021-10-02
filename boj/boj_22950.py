from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
m = input().strip()
k = int(input())

m = m[::-1]
res = 0
idx = m.find('1')
# print(idx, m)
idx = maxsize if idx==-1 else idx
res = idx>=k
print('YES' if res else 'NO')
