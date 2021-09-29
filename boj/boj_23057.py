from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import comb, sqrt, gcd
from bisect import *
from itertools import combinations

input = stdin.readline
setrecursionlimit(10**5)

n = int(input())
a = list(map(int, input().split()))

s = set()
tot = sum(a)
for choose in range(1, n+1):
    for combs in combinations(a, choose):
        s.add(sum(combs))
        
print(tot-len(s))