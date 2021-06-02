import sys

input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x


N = int(input())
M = int(input())
ans = []
ary = [list(map(int, input().split())) for i in range(N)]
parent = [i for i in range(N)]
plan = list(map(int, input().split()))

for i in range(0, N):
    for j in range(1+i, N):
        if ary[i][j] == 1:
            union(i, j)

ans = set([find(parent[i-1]) for i in plan])
if len(ans) == 1:
    print("YES")
else:
    print("NO")