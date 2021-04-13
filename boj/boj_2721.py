from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    r = 0
    n = int(input())
    for i in range(1,n+1):
        r += i*(i+1)*(i+2)//2
    print(r)