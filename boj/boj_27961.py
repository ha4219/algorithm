from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations
import math


MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

N = int(input())
# A = list(tuple(map(int, input().split())) for _ in range(N))


def main():
    n = N
    if n == 0:
        print(0);return
    if n == 1:
        print(1);return
    res = len(format(n, 'b'))
    
    res += 1 if int(format(n, 'b')[1:]) else 0
    print(res)
    return


if __name__ == '__main__':
    main()