from sys import stdin, maxsize, setrecursionlimit
from heapq import *
from collections import deque
import random

MAX = 17
MOD = 1000000007
setrecursionlimit(10**5)
input = stdin.readline

n = int(input())

a = [[] for _ in range(n+1)]
# parent = [[0] * (MAX+1) for _ in range(n+1)]
parent = [[[0, maxsize, -maxsize] for __ in range(MAX+1)] for _ in range(n+1)]
d = [0] * (n+1)

for _ in range(n-1):
    p, q, c = map(int, input().split())
    a[p].append((q, c))
    a[q].append((p, c))


def dfs(cur, depth):  # 변화 없음
    for next, next_cost in a[cur]:
        if d[next]:
            continue
        parent[next][0][0] = cur
        d[next] = depth + 1

        parent[next][0][1] = next_cost
        parent[next][0][2] = next_cost
        dfs(next, depth+1)
    return


# parent[1][0][0] = 0
d[1] = 0
dfs(1, 0)

# for i in range(1, n+1):
#     print(parent[i][0])

# parent[node][2^i 번째 parent 값]
for i in range(1, MAX):
    for j in range(1, n+1):
        # parent[j][i] = parent[parent[j][i-1]][i-1]
        parent[j][i][0] = parent[parent[j][i-1][0]][i-1][0]
        parent[j][i][1] = min(
            parent[j][i-1][1], parent[parent[j][i-1][0]][i-1][1])
        parent[j][i][2] = max(
            parent[j][i-1][2], parent[parent[j][i-1][0]][i-1][2])
        # print(i, parent[j][i][0], parent[j][i-1][0], j, parent[j][i][1:])

cache = {}


def solve(l, r):
    left, right = maxsize, -maxsize
    if d[l] > d[r]:
        l, r = r, l
    for i in range(MAX, -1, -1):
        if d[r] - d[l] >= (1 << i):
            left = min(left, parent[r][i][1])
            right = max(right, parent[r][i][2])
            r = parent[r][i][0]
    if l == r:
        return (left, right)
    for i in range(MAX, -1, -1):
        if parent[l][i][0] != parent[r][i][0]:
            left = min(left, parent[l][i][1], parent[r][i][1])
            right = max(right, parent[l][i][2], parent[r][i][2])

            l = parent[l][i][0]
            r = parent[r][i][0]
    left = min(left, parent[l][i][1], parent[r][i][1])
    right = max(right, parent[l][i][2], parent[r][i][2])
    return (left, right)


m = int(input())
for _ in range(m):
    p, q = map(int, input().split())
    print(*solve(p, q))


# for i in parent:
#     print(i[:5])
