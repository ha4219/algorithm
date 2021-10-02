from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n = int(input())

i = 1

while (i+1)*(2**(i+1))-1<n:
    i += 1
print(i)