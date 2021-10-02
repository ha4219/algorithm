from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)

d = {}
n = int(input())
for _ in range(n):
    x,y = map(int, input().split())
    if x==0:
        tmp = 'u' if y>0 else 'd'
    elif y==0:
        tmp = 'r' if x>0 else 'l'
    elif x>0 and y>0:
        tmp = '01'+str(y/x)
    elif x<0 and y>0:
        tmp = '02'+str(y/x)
    elif x<0 and y<0:
        tmp = '03'+str(y/x)
    else:
        tmp = '04'+str(y/x)
    val = d.get(tmp)
    if val == None:
        d[tmp] = 1
    else:
        d[tmp] += 1

print(max(d.values()))