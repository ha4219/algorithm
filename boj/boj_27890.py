import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline


x, N = map(int, input().split())

def main():
    global x
    for _ in range(N):
        if x & 1:
            x = (2*x) ^ 6
        else:
            x = (x//2) ^ 6
    print(x)
    return

if __name__ == '__main__':
    main()