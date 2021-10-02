from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)
v, e = map(int, input().split())
a = [[] for _ in range(v+1)]
for _ in range(e):
    p,q,r = map(int, input().split())
    a[p].append((q,r))
    a[q].append((p,r))

d = list(map(int, input().split()))

def dijkstra(start, end):
    pq = []
    # time , pos
    visit = [maxsize] * (v+1)
    visit[start] = 0
    heappush(pq, (0, start))
    while pq:
        time, pos = heappop(pq)
        if time>visit[pos]:
            continue
        for next, err in a[pos]:
            if visit[next] > err+time:
                visit[next] = err+time
                heappush(pq, (visit[next], next))
    return visit[end]

start = int(input())
res = []
yo = 0
prev = d[0]
for i in range(10):
    # yo : prev -> d[i] 까지 가는데 걸리는 시간
    tmp = dijkstra(prev, d[i])
    if tmp==maxsize:
        continue
    # 시간은 누적해야함
    yo += tmp
    # 내가 start에서 요구르트 아줌마 목적지 까지 걸리는 시간
    my = dijkstra(start, d[i])
    prev = d[i]
    # print(yo, my)
    if yo>=my:
        res.append(d[i])

# print(res)
print(min(res) if res else -1)