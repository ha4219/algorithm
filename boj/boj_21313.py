from sys import stdin


input = stdin.readline

n = int(input())


if n%2:
    n-=3
    print(1,end='')
    for i in range(1,n):
        if i%2:
            print(' 2',end='')
        else:
            print(' 1',end='')
    print(' 1 2 3')
else:
    print(1,end='')
    for i in range(1,n):
        if i%2:
            print(' 2',end='')
        else:
            print(' 1',end='')
    print()
