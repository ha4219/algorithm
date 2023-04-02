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

N, M = map(int, input().split())
a = list(map(int, input().split()))


def main():
    s = [0] * N
    s[0] = a[0]

    pq = [-a[0]]
    cnt = 0

    if s[0] >= M:
        s[0] += 2 * heappop(pq)
        cnt += 1

    for i in range(1, N):
        s[i] = s[i-1] + a[i]
        heappush(pq, -a[i])
        while pq and  s[i] >= M:
            x = heappop(pq)
            s[i] += x * 2
            cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
