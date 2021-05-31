from sys import stdin, setrecursionlimit, maxsize
from math import ceil,log2


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
if n==1:
    print(1)
    print(1, 1)
else:
    print(n*2-2)
    for i in range(1,n+1):
        print(i, 1)
    for i in range(2,n):
        print(i, n)