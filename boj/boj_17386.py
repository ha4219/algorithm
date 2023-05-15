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
p = []

def ccw(pos1, pos2, pos3) -> int:
    x1, y1 = pos1
    x2, y2 = pos2
    x3, y3 = pos3
    return x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1

def main():
    for i in a:
        p.append((i[0], i[1]))
        p.append((i[2], i[3]))
    
    # print(ccw(p[0], p[1], p[2]), ccw(p[0], p[1], p[3]))
    # print(ccw(p[2], p[3], p[0]), ccw(p[2], p[3], p[1]))
    ans = ccw(p[0], p[1], p[2]) * ccw(p[0], p[1], p[3]) < 0 and ccw(p[2], p[3], p[0]) * ccw(p[2], p[3], p[1]) < 0

    print(1 if ans else 0)
    return


if __name__ == '__main__':
    main()