from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    MAX = n*2+1
    v = [-1] * MAX
    res = 0
    for i in range(n):
        v[a[i]] = i+1

    for i in range(3,MAX):
        j = 1
        while j*j<=i:
            if i%j==0 and j*j!=i and v[j]!=-1 and v[i//j]!=-1 and v[j]+v[i//j]==i:
                res += 1
            j+=1
    print(res)