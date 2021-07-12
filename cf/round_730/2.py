from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import gcd


input = stdin.readline
# setrecursionlimit(10**6)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    s = sum(a)
    k = s%n
    print(k*(n-k))
    