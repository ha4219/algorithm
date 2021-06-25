from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    