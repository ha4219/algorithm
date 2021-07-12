from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import gcd


input = stdin.readline
# setrecursionlimit(10**6)
MOD = 10**9+7

def lcm(x,y):
    return x//gcd(x,y)*y

for _ in range(int(input())):
    n = int(input())
    g = 1
    res = 0
    for i in range(1,n+1):
        g = lcm(g,i)
        if g>n:
            break
        res += n//g
    print((res+n)%MOD)