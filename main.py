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


N = int(input())
a =[[] for _ in range(N)]

for _ in range(N-1):
    l, r = map(int, input().split())
    a[l-1].append(r-1)
    a[r-1].append(l-1)

leaf = set()
d1 = [maxsize] * N
d2 = [maxsize] * N
d3 = [maxsize] * N

qs = list(map(int, input().split()))

def dfs(cur, depth, d):
    if len(a[cur]) == 1:
        leaf.add(cur)
    for nn in a[cur]:
        if d[nn] > depth+1:
            d[nn] = depth+1
            dfs(nn, depth+1, d)

d1[qs[0]-1] = 0
dfs(qs[0]-1, 0, d1)

d2[qs[1]-1] = 0
dfs(qs[1]-1, 0, d2)

d3[qs[2]-1] = 0
dfs(qs[2]-1, 0, d3)

def main():
    for i in leaf:
        if d1[i] < d2[i] and d1[i] <d3[i]:
            print('YES')
            return
    print('NO')
    return
    


if __name__ == '__main__':
    main()