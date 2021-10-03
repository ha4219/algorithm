from sys import stdin, maxsize
from heapq import *

input = stdin.readline

MOD = 3628800

n, m = map(int, input().split())

d = [[] for _ in range(n+1)]


for _ in range(m):
    s,e,l,k = map(int, input().split())
    d[s].append((e,l*MOD,k))
    d[e].append((s,l*MOD,k))

def dijkstra():
    pq = [(0, 1, 1)]
    v = [[maxsize] * 11 for _ in range(n+1)]
    v[1][1] = 0
    while pq:
        t, pos, sp = heappop(pq)
        # if pos == n:
        #     return t
        if v[pos][sp] < t:
            continue
        for to, l, k in d[pos]:
            for alpha in range(-1 , 2):
                next_speed = sp+alpha
                if not (1<=next_speed and next_speed<=k):
                    continue
                next_cost = t + l//next_speed
                if  v[to][next_speed]>next_cost:
                    v[to][next_speed]=next_cost
                    heappush(pq, (next_cost, to, next_speed))
    return min(v[n])

res = dijkstra()
print(res//MOD, end='')
print(('%.9f'%round((res % MOD)/MOD,9))[1:])