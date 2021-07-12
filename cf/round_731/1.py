from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import gcd


input = stdin.readline
# setrecursionlimit(10**6)
MAX = 1001

dx, dy = (1,-1,0,0),(0,0,1,-1)


for _ in range(int(input())):
    input()
    sx, sy = map(int,input().split())
    ex, ey = map(int,input().split())
    fx, fy = map(int,input().split())

    if (sx==ex==fx and (sy<fy<ey or ey<fy<sy)) or (sy==ey==fy and (sx<fx<ex or ex<fx<sx)):
        print(abs(ex-sx)+abs(ey-sy)+2)
    else:
        print(abs(ex-sx)+abs(ey-sy))
    
