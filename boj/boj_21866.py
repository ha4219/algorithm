from sys import stdin, setrecursionlimit, maxsize


setrecursionlimit(10**6)
input = stdin.readline

a = list(map(int,input().split()))
t = 100
res = 1
ret = 0
n = 9
for i in range(n):
    if t*(i//2+1)<a[i]:
        res = 0
        break
    ret += a[i]

if res:
    if ret<t:
        print('none')
    else:
        print('draw')
else:
    print('hacker')