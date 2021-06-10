from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))
a.sort()
print(*a)