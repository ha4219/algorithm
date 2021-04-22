from sys import stdin


input = stdin.readline


for _ in range(int(input())):
    t,a=input().split()
    t=int(t)
    print(a[:t-1]+a[t:])