from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)


res1 = 0
res2 = ''
for _ in range(int(input())):
    for __ in range(int(input())):
        s, nn = input().split()
        nn = int(nn)
        if nn>res1:
            res1 = nn
            res2 = s
    print(res2)
    