from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    a,b=map(int,input().split())
    print(a*a//b//b)