from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

def f(n):
    if n==2:
        return [2,1]
    res = []
    idx = 1
    if n&1 and n>=3:
        res = [3,1,2]
        idx = 4
    for i in range(idx, n, 2):
        res.append(i+1)
        res.append(i)
    return res

for _ in range(int(input())):
    n = int(input())
    print(*f(n))