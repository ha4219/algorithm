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

s = input().strip()
n = int(input())
p = [[0] * 27 for _ in range(len(s)+1)]

for i, c in enumerate(s):
    p[i+1][ord(c) - ord('a')] += 1
    if i == 0:
        continue
    for j in range(27):
        p[i+1][j] += p[i][j]

for _ in range(n):
    c, l, r = input().split()
    l, r = int(l), int(r)
    print(p[r+1][ord(c)-ord('a')]-p[l][ord(c)-ord('a')])
