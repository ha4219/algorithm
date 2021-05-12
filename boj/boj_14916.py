from sys import stdin, maxsize, setrecursionlimit


input = stdin.readline

n = int(input())
res = maxsize
for i in range(0,n+1,5):
    if (n-i)%2==0:
        res = min(res, i//5+(n-i)//2)
print(-1 if res==maxsize else res)