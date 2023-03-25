import enum
from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline


N, M = map(int, input().split())
a = [int(input()) for _ in range(M)]
d = [1 if x % 10 == 0 or x % 10 == 3 or x % 10 == 6 else 0 for x in range(N)]

def main():
    res = sum(d)
    for q in a:
        if d[q-1]:
            res -= 1
            d[q-1] = 0
        else:
            res += 1
            d[q-1] = 1
        print(res)


if __name__ == '__main__':
    main()