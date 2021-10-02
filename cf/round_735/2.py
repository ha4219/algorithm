from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)
MAX = 100
p = [1] * MAX
p[0] = 0
p[1] = 0

for i in range(2, MAX):
    if p[i]==0:
        continue
    for j in range(i*2, MAX, i):
        p[j] = 0

def solve(s, k):
    for i in range(k):
        if s[i]=='1' or s[i]=='4' \
            or s[i]=='6' or s[i]=='8' or s[i]=='9':
            print(1)
            print(s[i])
            return 0
    for i in range(k):
        for j in range(i+1, k):
            if p[int(s[i])*10+int(s[j])]==0:
                print(2)
                print(s[i]+s[j])
                return 0

for _ in range(int(input())):
    k = int(input())
    s = input().strip()
    solve(s, k)

