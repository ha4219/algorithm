from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**9)
input = stdin.readline

s = input().strip()
sl2 = len(s)//2
print(s[:sl2],s[sl2:])
