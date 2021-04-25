from sys import stdin


input = stdin.readline

d = [i for i in range(1,21)]
for _ in range(10):
    a,b=map(int,input().split())
    if a==1:
        d[a-1:b] = d[b-1::-1]
    else:
        d[a-1:b] = d[b-1:a-2:-1]
print(*d)