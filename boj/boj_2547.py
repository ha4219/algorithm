from sys import stdin


input = stdin.readline

for _ in range(int(input())):
    input()
    n=int(input())
    r = 0
    for _ in range(n):
        r += int(input())%n
        r%=n
    print("YES" if r==0 else "NO")