from sys import stdin, maxsize, setrecursionlimit


input = stdin.readline

<<<<<<< HEAD
n = int(input())
res = maxsize
for i in range(0,n+1,5):
    if (n-i)%2==0:
        res = min(res, i//5+(n-i)//2)
print(-1 if res==maxsize else res)
=======
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
>>>>>>> cc38fde37ef623a98d6498bcf7707fc6c5eeba17
