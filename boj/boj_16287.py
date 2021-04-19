from sys import stdin


input = stdin.readline

w,n=map(int,input().split())
a=list(map(int,input().split()))

d = [0] * (10**6+1)

# for k in range(4):
def solve():
    for i in range(n):
        for j in range(i+1,n):
            if a[i]+a[j]>w:
                continue
            if d[w-a[i]-a[j]]:
                return 1
        for j in range(i):
            if a[i]+a[j]<w:
                d[a[i]+a[j]]=1
    return 0
print('YES' if solve() else 'NO')