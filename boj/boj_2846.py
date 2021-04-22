from sys import stdin


input = stdin.readline


n = int(input())
a=list(map(int,input().split()))
res = 0
prev = a[0]
cur_size = 0
for i in range(1,n):
    if prev < a[i]:
        cur_size += a[i]-prev
        prev = a[i]
        res = max(cur_size, res)
    else:
        prev = a[i]
        cur_size = 0
print(res)
