from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
s = input().strip()
print(s[n-5:])