from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

def round2(n):
	return int(n) + 1 if n - int(n) >= 0.5 else int(n)


n = int(input())
a = [int(input()) for _ in range(n)]
a.sort()
nn = round2(n*0.15)
res = 0
t = 0
for i in range(nn,n-nn):
    t += 1
    res += a[i]
if n==0:
    print(0)
else:
    print(round2(res/t))