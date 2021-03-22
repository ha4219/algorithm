from sys import stdin


input = stdin.readline

n = int(input())
a = []

for i in range(n):
    t=input().split()
    a.append((int(t[0]),i,t[1]))
a.sort()
for i in range(n):
    print(a[i][0],a[i][2])