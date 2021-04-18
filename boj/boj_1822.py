from sys import stdin


input = stdin.readline

n,m=map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
t=a-b
t=sorted(t)
print(len(t))
print(*t)