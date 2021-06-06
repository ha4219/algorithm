from sys import stdin, setrecursionlimit, maxsize

input = stdin.readline
setrecursionlimit(10**6)
n,m = map(int,input().split())
a = [0]+list(map(int,input().split()))

# def f1(idx):
#     for i in range(1,n+1):
#         if i%idx==0:
#             a[i] ^= 1

# def f2(idx):
#     l = 1
#     while idx-l>0 and idx+l<=n and a[idx-l]==a[idx+l]:
#         a[idx-l] ^= 1
#         a[idx+l] ^= 1
#         l += 1

for _ in range(m):
    t = list(map(int,input().split()))
    if t[0] == 1:
        a[t[1]] = t[2]
    elif t[0] == 2:
        for i in range(t[1],t[2]+1):
            a[i] ^= 1
    elif t[0] == 3:
        for i in range(t[1],t[2]+1):
            a[i] = 0
    else:
        for i in range(t[1],t[2]+1):
            a[i] = 1
print(*a[1:])