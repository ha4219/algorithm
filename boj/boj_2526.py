from sys import stdin


input = stdin.readline

n,p=map(int,input().split())

MAX = 1001
d = [0] * MAX

def solve():
    prev = 0
    nn = n
    while not d[nn]:
        d[nn] = d[prev] + 1
        prev = nn
        nn = (nn * n) % p
    return d[prev]-d[nn]+1
print(solve())