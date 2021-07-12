from sys import stdin, setrecursionlimit, maxsize
# from collections import deque



input = stdin.readline
# setrecursionlimit(10**6)


for _ in range(int(input())):
    n,a,b = map(int,input().split())
    res = 0
    if a==1:
        if (n-1)%b==0:
            res = 1
    else:
        x = 1
        while x<=n:
            if x%b==n%b:
                res = 1
                break
            x *= a
    print('Yes' if res else 'No')
        