from sys import stdin



input = stdin.readline

a = [input().strip() for _ in range(3)]
al = [len(a[i]) for i in range(3)]
INIT = 0
MAX = 101
d = [[[INIT]*MAX for _ in range(MAX)] for __ in range(MAX)]

for i in range(al[0]):
    for j in range(al[1]):
        for k in range(al[2]):
            if a[0][i]==a[1][j]==a[2][k]:
                print(i,j,k)
                d[i][j][k] = d[i-1][j-1][k-1] + 1
            else:
                d[i][j][k] = max(d[i-1][j][k], max(d[i][j-1][k], d[i][j][k-1]))

print(d[al[0]-1][al[1]-1][al[2]-1])