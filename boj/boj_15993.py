from sys import stdin


input = stdin.readline

MAX = 100001
MOD = 10**9+9
d = [[0]*2 for _ in range(MAX)]
d[1][1] = 1
d[2][1] = 1
d[2][0] = 1
d[3][1] = 2
d[3][0] = 2
for i in range(4, MAX):
    d[i][0] = (d[i-1][1] + d[i-2][1] + d[i-3][1])%MOD
    d[i][1] = (d[i-1][0] + d[i-2][0] + d[i-3][0])%MOD
for _ in range(int(input())):
    t=int(input())
    print(d[t][1],d[t][0])