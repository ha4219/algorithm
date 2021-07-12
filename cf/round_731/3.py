from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from math import exp, gcd


input = stdin.readline
# setrecursionlimit(10**9)


for __ in range(int(input())):
    input()
    k,n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    