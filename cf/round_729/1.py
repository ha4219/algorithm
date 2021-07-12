from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
# setrecursionlimit(10**6)


for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))

    odd = 0
    even = 0
    for i in range(2*n):
        if a[i]%2:
            odd += 1
        else:
            even += 1
    if odd==even:
        print('Yes')
    else:
        print('No')