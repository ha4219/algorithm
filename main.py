from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
