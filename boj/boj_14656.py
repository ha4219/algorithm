from sys import stdin


input = stdin.readline

n = int(input())
a = list(map(int,input().split()))
r = 0
for i in range(1,n+1):
    if i!=a[i-1]:
        r+=1
print(r)