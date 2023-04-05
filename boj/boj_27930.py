import enum
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

s = input().strip()


def main():
    ko = 'KOREA'
    yo = 'YONSEI'
    k = -1
    y = -1

    v = 0
    for c in ko:
        v = v + s[v:].find(c)
        # print(v, c)
        if v == -1:
            k = maxsize
            break
        else:
            k = max(k, v)

    v = 0
    for c in yo:
        v = v + s[v:].find(c)
        # print(v, c)
        if v == -1:
            y = maxsize
            break
        else:
            y = max(y, v)
    print(yo if y < k else ko)
    return

if __name__ == '__main__':
    main()