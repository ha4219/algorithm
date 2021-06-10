from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())
a = input().strip()

res = 1
for i in range(1,n*2):
    if a[i]==a[i-1]:
        res = 0
        break
print('Yes' if res else 'No')