from sys import stdin


input = stdin.readline


n = int(input())
a=list(map(int,input().split()))
res = []
for i,v in enumerate(a):
    res.insert(v,i+1)
print(*res[::-1])