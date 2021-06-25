from sys import stdin, setrecursionlimit, maxsize


input = stdin.readline
setrecursionlimit(10**6)


while True:
    n = int(input())
    if n==-1:
        break
    res = []
    ret = 0
    for i in range(1,n):
        if n%i==0:
            res.append(i)
            ret += i
        if n<ret:
            break
    if ret==n:
        print(n,'=',' + '.join(map(str,res)))
    else:
        print(n,'is NOT perfect.')