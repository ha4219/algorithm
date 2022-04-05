from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from itertools import combinations
from collections import deque
import random
import math

MAX = 17
MOD = 1000000000007
MOD2 = MOD * 2
setrecursionlimit(10**5)
input = stdin.readline


def dijkstra(start):
    d = [maxsize] * (n+1)
    d[start] = 0
    pq = [(0, start)]
    while pq:
        cost, cur = heappop(pq)
        for next, next_cost in a[cur]:
            if d[next] <= cost + next_cost:
                continue
            d[next] = cost + next_cost
            heappush(pq, (d[next], next))
    return d


for ____ in range(int(input())):
    n, m, t = map(int, input().split())
    a = [[] for _ in range(n+1)]
    s, g, h = map(int, input().split())
    road = -1
    for _ in range(m):
        p, q, c = map(int, input().split())
        a[p].append((q, c))
        a[q].append((p, c))
        if (g == p and h == q) or (h == p and g == q):
            road = c

    ends = [int(input()) for _ in range(t)]

    all_path = dijkstra(s)
    l, r = (g, h) if all_path[g] < all_path[h] else (h, g)

    half_path = dijkstra(r)

    res = []
    for end in ends:
        if all_path[r] + half_path[end] == all_path[end]:
            res.append(end)
    res.sort()
    print(*res)
