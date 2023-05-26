from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from bisect import *
from collections import deque
import random
from itertools import combinations, permutations
import math


MAX = 17
MOD = 1000000007
setrecursionlimit(10**6)
input = stdin.readline

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(2)]

def main():
    wait = [(-1, 0)] # prev, val, 
    for _ in range(N):
        q = []
        for (p, v) in wait:
            for l in range(3):
                if p == l:
                    q.append((l, v + a[0][l]//2))
                    q.append((l, v + a[1][l]//2))
                else:
                    q.append((l, v + a[0][l]))
                    q.append((l, v + a[1][l]))
        wait = q
    res = 0
    for (_, val) in q:
        res += 1 if val >= M else 0
    print(res)
    return


if __name__ == "__main__":
    main()
