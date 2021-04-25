from sys import stdin


input = stdin.readline

a = [str((i+6)%10) for i in range(10)]
b = [chr((i+8)%12+ord('A')) for i in range(12)]

def solve(t):
    return b[t%12]+a[t%10]
print(solve(int(input())))
