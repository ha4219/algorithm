from sys import stdin, maxsize
from math import *


input = stdin.readline
def dist(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

n = int(input())
a = [list(map(float, input().split())) for _ in range(n)]
rep = [0,0]
res = maxsize

for i in range(n):
    tmp = 0
    for j in range(n):
        tmp = max(tmp, dist(a[i][0],a[i][1],a[j][0],a[j][1]))
    if res >= tmp:
        res = tmp
        rep = a[i]
print(*rep)