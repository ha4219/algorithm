from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)

n = int(input())

if n&1:
    print('*'*n)
    for i in range(n//2+1):
        if i==0:
            print(' '*(n//2)+'*')
        else:
            t = n//2-i
            print(' '*(t)+'*'+' '*((i-1)*2+1)+'*')

else:
    print('I LOVE CBNU')