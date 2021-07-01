from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n, m = map(int,input().split())
n, m = m, n
a = list(map(int,input().split()))

def f(l):
    cnt = 0
    for i in range(n):
        if a[i]>=l:
            cnt += a[i]//l
    # print(l, cnt)
    return cnt>=m

l = 1
r = 1000000000
res = 0

while l<=r:
    mid = (l+r)//2
    if f(mid):
        res = max(res, mid)
        l = mid + 1
    else:
        r = mid - 1
print(res)