from sys import stdin, setrecursionlimit, maxsize
from math import gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 1000001

# n = int(input())
# a = list(map(int,input().split()))
p = [1] * MAX
p[1] = 0
p[2] = 0

for i in range(2,1001):
    for j in range(i*2,MAX,i):
        p[j] = 0
print(p[:100])