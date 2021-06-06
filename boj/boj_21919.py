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

for i in a:
    if p[i] and res%i:
        res *= i
if res == 1:
    print(-1)
else:
    print(res)