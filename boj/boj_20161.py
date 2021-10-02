from sys import stdin, setrecursionlimit, maxsize
from collections import deque
from heapq import *
from math import sqrt, gcd


input = stdin.readline
setrecursionlimit(10**6)
MAX = 100005

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    a[i] ^= b[i]

d = [[-1]*((2**k)+1) for _ in range(n+1)]

K = (1<<k) - 1
path = 0
for i in range(k):
    if a[i]:
        path |= (1<<i)

def dfs(idx, path, score):
    print('in', idx, bin(path)[2:], d[idx][path], score)
    if idx+k==n+1:
        if path==0:
            return score
        else:
            return maxsize
    if d[idx][path]!=-1:
        return d[idx][path]
    # print('in', idx, bin(path)[2:])
    d[idx][path] = maxsize
    tmp_path = path ^ K
    
    # pass
    if path&1==0:
        # print('next', idx, bin(path)[2:])
        if idx<n-k and a[idx+k]==1:
            d[idx][path] = min(d[idx][path], dfs(idx+1, (path>>1)|(1<<(k-1)), score))
            # print('next 1', idx, bin(path)[2:], bin((path>>1)|(1<<(k-1)))[2:])
        else:
            d[idx][path] = min(d[idx][path], dfs(idx+1, path>>1, score))
            # print('next 2', idx, bin(path)[2:], bin(path>>1)[2:])

    # ppang
    for i in range(k):
        ppath = tmp_path ^ (1<<i)
        d[idx][path] = min(d[idx][path], dfs(idx,ppath, score+1))
    
    
    return d[idx][path]

def dijkstra(idx, path, score):
    pq = []
    heappush(pq, (score, idx, path))
    while pq:
        score, idx, path = heappop(pq)
        if idx+k==n+1:
            if path==0:
                return score
            else:
                continue
        if d[idx][path]!=-1:
            continue
        d[idx][path] = maxsize
        tmp_path = path^K

        for i in range(k):
            ppath = tmp_path^(1<<i)
            heappush(pq, (score+1, idx, ppath))

        if path&1==0:
            if idx<n-k and a[idx+k]==1:
                heappush(pq, (score, idx+1, (path>>1)|(1<<(k-1))))
            else:
                heappush(pq, (score, idx+1, path>>1))
    return -1


print(dijkstra(0, path, 0))