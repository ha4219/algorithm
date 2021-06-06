from sys import stdin, setrecursionlimit, maxsize
from math import gcd


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))
x = int(input())

res = 0
ret = 0
for i in a:
    if gcd(i, x)==1:
        res += i
        ret += 1
print(res/ret)