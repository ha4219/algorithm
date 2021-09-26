from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)

n, t = map(int, input().split())

a = []

for _ in range(n):
    s,x,y = map(int, input().split())
    a.append((s,x,y))

d = [[maxsize]*n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                d[i][j] = 0
            elif d[i][j]==maxsize:
                if a[i][0] and a[j][0]:
                    d[i][j] = t
                d[i][j] = min(abs(a[i][1]-a[j][1]) + abs(a[i][2]-a[j][2]), d[i][j])
            else:
                if a[i][0] and a[j][0]:
                    d[i][j] = min(t, d[i][j])
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])


for _ in range(int(input())):
    x,y=map(int,input().split())
    print(d[x-1][y-1])