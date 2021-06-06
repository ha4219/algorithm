from sys import stdin, setrecursionlimit, maxsize
from math import gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 1000001

n = int(input())
a = list(map(int,input().split()))
p = [1] * MAX
p[0] = 0
p[1] = 0

for i in range(2,1001):
    for j in range(i*2,MAX,i):
        p[j] = 0

res = 1
ret = 0
g = 1
f = 1

for i in a:
    if p[i]:
        res *= i
        ret += 1
        if f:
            g = i
            f = 0
        else:
            g = gcd(g, i)
if ret == 0:
    print(-1)
else:
    print(res//g)