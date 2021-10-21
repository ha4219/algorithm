from sys import stdin, maxsize, setrecursionlimit
from heapq import *

setrecursionlimit(10**5)
input = stdin.readline

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    a = [[] for _ in range(n+1)]
    for _ in range(m):
        p,q,r = map(int, input().split())
        a[p].append((q, r))
        a[q].append((p, r))
        if (p==g and q==h) or (p==h and q==g): tmp = r

    can = [int(input()) for _ in range(t)]
    can.sort()
    d = [maxsize] * (n+1)
    d[s] = 0
    pq = [(0, s)]
    while pq:
        cost, cur = heappop(pq)
        if d[cur]<cost:
            continue
        for next in a[cur]:
            if(d[next[0]]<cost+next[1]): continue
            d[next[0]] = cost+next[1]
            heappush(pq, (d[next[0]], next[0]))
    d1 = [maxsize] * (n+1)
    l, r = (g, h) if d[g]<d[h] else (h, g)
    d1[r] = 0
    pq = [(0, r)]
    while pq:
        cost, cur = heappop(pq)
        if d1[cur]<cost:
            continue
        for next in a[cur]:
            if(d1[next[0]]<cost+next[1]): continue
            d1[next[0]] = cost+next[1]
            heappush(pq, (d1[next[0]], next[0]))
    res = []
    for num in can:
        if d[num]==d[l]+d1[num]+tmp:
            res.append(num)
    print(*res)
