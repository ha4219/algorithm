from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd, ceil


input = stdin.readline
setrecursionlimit(10**5)

def solution(n, s):
    if n==1:
        return s
    n2 = n//2+1
    return s//n2


for _ in range(int(input())):
    p,q=map(int,input().split())
    print(solution(p,q))