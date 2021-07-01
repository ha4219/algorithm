from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    MAX = n*2+1
    v = [0] * MAX
    res = 0
    for i in range(n):
        print(a[i])

    print(res)