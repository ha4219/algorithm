from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)


def get_sum(l, r):
    if l>r:
        return 0
    return p[r]-p[l-1] if l%2 else p[l-1]-p[r]

for _ in range(int(input())):
    n, q = map(int, input().split())
    s = input().strip()
    a = [0] * (n+1)
    p = [0] * (n+1)
    for i in range(1,n+1):
        a[i] = 1 if s[i-1]=='+' else -1
    for i in range(1, n+1):
        p[i] = p[i-1] + (a[i] if i%2==1 else -a[i])
    for _ in range(q):
        l,r = map(int, input().split())
        if get_sum(l, r)==0:
            print(0)
            continue
        if (r-l+1)%2==0:
            print(2)
        else:
            print(1)
