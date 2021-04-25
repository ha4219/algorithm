from sys import stdin


input = stdin.readline

a,b,c,n=map(int,input().split())
MAX = 301
def f():
    for i in range(MAX):
        if a*i>n:
            break
        for j in range(MAX):
            if a*i+b*j>n:
                break
            for k in range(MAX):
                if a*i+b*j+c*k>n:
                    break
                if a*i+b*j+c*k==n:
                    return 1
    return 0
print(f())