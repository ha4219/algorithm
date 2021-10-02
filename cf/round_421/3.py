from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**5)


for _ in range(int(input())):
    n = int(input())
    s = input().strip()

    solved = 0
    for i in range(n):
        if s[i]=='0':
            solved = 1
            if i>=n//2:
                print(1, i+1, 1, i)
                break
            else:
                print(i+2, n, i+1, n)
                break
    if solved==0:
        print(1, n-1, 2, n)