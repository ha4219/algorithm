from sys import stdin, setrecursionlimit


setrecursionlimit(10**6)

input = stdin.readline

def f(a):
    if a == p[a]:
        return a
    b = f(p[a])
    w[a] += w[p[a]]
    p[a] = b
    return b

while 1:
    n,m = map(int,input().split())
    if n==m and m==0:
        break
    w = [0] * (n+2)
    p = [i for i in range(n+1)]
    for _ in range(m):
        cmd = list(input().split())
        if cmd[0]=='!':
            a,b,c=map(int, cmd[1:])
            l = f(a)
            r = f(b)
            if l!=r:
                p[l] = r
                w[l] = w[b] - w[a] + c
        else:
            a,b=map(int, cmd[1:])
            l = f(a)
            r = f(b)
            if l!=r:
                print('UNKNOWN')
                continue
            else:
                print(w[a]-w[b])
        
