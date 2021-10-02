from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)


d = {}

for i in range(int(input())):
    p, n = input().split()
    n = int(n)
    d[n] = p
print(d[min(d.keys())])