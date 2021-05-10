from sys import stdin, maxsize, setrecursionlimit


setrecursionlimit(10**6)
input = stdin.readline

while 1:
    a = list(map(int,input().split()))
    if a[0]==0:
        break
    d = []
    for i in range(a[0]):
        try:
            if d[-1]!=a[i+1]:
                d.append(a[i+1])
        except:
            d.append(a[i+1])
    print(*d,'$')