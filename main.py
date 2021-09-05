from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
a.sort()
