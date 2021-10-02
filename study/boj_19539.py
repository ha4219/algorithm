from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt


input = stdin.readline
setrecursionlimit(10**6)


s = ''
for i in range(1,1000):
    s+=str(i)
print(s)