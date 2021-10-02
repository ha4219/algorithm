from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

x1,y1,r1 = map(int,input().split())
x2,y2,r2 = map(int,input().split())

dis1 = (x1-x2)**2+(y1-y2)**2
dis2 = (r1+r2)**2
res = dis1<dis2
print('YES' if res else 'NO')