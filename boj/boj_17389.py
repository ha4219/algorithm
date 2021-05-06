from sys import stdin

input = stdin.readline

n = int(input())
s = input().strip()

res = 0
acc = 0

for i in range(n):
    if s[i]=='O':
        res += (i+1+acc)
        acc += 1
    else:
        acc = 0
print(res)
