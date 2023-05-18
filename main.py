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
a = [list(map(int, input().split())) for _ in range(N)]
# p = [tuple(map(int, input().split())) for _ in range(3)]


def ccw(p1, p2, p3) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    res = x2 * y3 - x3 * y2 - x1 * y3 + x3 * y1 + x1 * y2 - x2 * y1
    return res if res == 0 else (1 if res > 0 else -1)


def main():
    p = sorted(a, key=lambda x: x[4])  # O(nlogn)
    res = 0

    for i in range(N):  # O(n^2)
        p0, p1, w = (p[i][0], p[i][1]), (p[i][2], p[i][3]), p[i][4]
        m = 0
        for j in range(i + 1, N):
            p2, p3, _ = (p[j][0], p[j][1]), (p[j][2], p[j][3]), p[j][4]
            l, r = ccw(p0, p1, p2) * ccw(p0, p1, p3), ccw(p2, p3, p0) * ccw(p2, p3, p1)
            m += 1 if l < 0 and r < 0 else 0
        res += w * (m + 1)
    # if l == 0 and r == 0:  # 일직선
    #     ans = max(p[0], p[1]) >= min(p[2], p[3]) and max(p[2], p[3]) >= min(p[0], p[1])
    #     print(1 if ans else 0)
    #     return
    print(res)
    return


if __name__ == "__main__":
    main()
