from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

for _ in range(int(input())):
    l, r = map(int, input().split())
    
    if r<l*2:
        print(r-l)
    else:
        print((r-1)//2)
        