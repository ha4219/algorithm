from sys import stdin, setrecursionlimit, maxsize
from math import ceil,floor,gcd


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = list(map(int,input().split()))

s = [0] * (n+1)

def q(i):
    res = 0
    while i>0:
        res += s[i]
        i &= (i-1)
    return res

def u(i,v):
    while i<n+1:
        s[i] += v
        i += (i&-i)

res = 0
for i in range(n):
    res += (i-q(a[i]))
    # print(i-q(a[i]), a[i], q(a[i]))
    u(a[i], 1)
print(res)