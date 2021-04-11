from sys import stdin,maxsize


input = stdin.readline

def f():
    for i in range(1,n+1):
        for j in range(1,n+1):
            for next,time in a[j]:
                if d[next]>d[j]+time:
                    d[next]=d[j]+time
                    if i==n:
                        return True
    return False

for ppp in range(int(input())):
    n,m,w=map(int,input().split())
    a = [[] for _ in range(n+1)]

    for _ in range(m):
        p,q,r=map(int,input().split())
        a[p].append((q,r))
        a[q].append((p,r))
    for _ in range(w):
        p,q,r=map(int,input().split())
        a[p].append((q,-r))
    d = [maxsize] * (n+1)
    d[1] = 0
    print('YES' if f() else 'NO')