from sys import stdin


input = stdin.readline

n = int(input())

a = []
for _ in range(n):
    t=int(input())
    a.append([t,1])

s=[]
i = 0
res = 0
while i<n:
    if not s:
        s.append(a[i])
        i += 1
    else:
        if s[-1][0]>a[i][0]:
            res += 1
            s.append(a[i])
            i+=1
        elif s[-1][0]==a[i][0]:
            a[i][1] += s[-1][1]
            res += s[-1][1]
            s.pop()
        else:
            res += s[-1][1]
            s.pop()
print(res)