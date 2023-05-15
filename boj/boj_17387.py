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

# N = int(input())
a = [list(map(int, input().split())) for _ in range(2)]
# p = [tuple(map(int, input().split())) for _ in range(3)]
p = []

def ccw(p1,p2,p3) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1

def main():
    global p
    for i in a:
        p.append((i[0], i[1]))
        p.append((i[2], i[3]))

    l, r = ccw(p[0], p[1], p[2]) * ccw(p[0], p[1], p[3]), ccw(p[2], p[3], p[0]) * ccw(p[2], p[3], p[1])
    
    if l == 0 and r == 0: # 일직선
        ans = max(p[0], p[1]) >= min(p[2], p[3]) and max(p[2], p[3]) >= min(p[0], p[1])
        print(1 if ans else 0)
        return
    ans = l <= 0 and r <= 0
    print(1 if ans else 0)
    return


if __name__ == '__main__':
    main()