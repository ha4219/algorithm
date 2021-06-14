from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**9)
input = stdin.readline

def f(s):
    sl = len(s)
    for i in range(sl//2):
        if s[i]!=s[sl-i-1]:
            return 0
    return int(s)

n = int(input())
a = list(input().split())
res = 0
for i in a:
    res += f(i)
print(res)