from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
# setrecursionlimit(10**6)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    res = []
    ret = a[0]
    for i in range(1,n):
        res.append((a[i-1]^a[i])^a[i])
    print(*res)
