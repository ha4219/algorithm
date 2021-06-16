from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = list(map(int,input().split()))

l=0
rmax = a[0]
rmin = a[0]

def find():
    p = q = 0
    for i in range(1,11):
        if ra[i]:
            q = i
            break
    for i in range(1,11):
        if ra[11-i]:
            p = 11-i
            break
    return (p,q)

ra = [0] * 11

res = 0

for r in range(n):
    ra[a[r]] += 1
    rmax,rmin = find()
    while rmax-rmin>2 and l<r:
        ra[a[l]] -= 1
        rmax,rmin = find()
        l += 1
    print(l,r, a[l:r+1],rmin,rmax)
    res = max(res, r-l+1)
print(res)