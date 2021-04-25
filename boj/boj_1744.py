from sys import stdin

input = stdin.readline


n = int(input())
a = []
b = []
an=0
bn=0
for _ in range(n):
    t = int(input())
    if t>0:
        a.append(t)
        an += 1
    else:
        b.append(t)
        bn += 1
a.sort(reverse=True)
b.sort()
res = 0
i = 0
while i<an:
    if i!=an-1 and a[i]<0 and a[i]*a[i+1]>0:
        res += a[i]*a[i+1]
        i += 1
    elif i!=an-1 and a[i+1]>1:
        res += a[i]*a[i+1]
        i += 1
    else:
        res += a[i]
    i+=1

i = 0
while i<bn:
    if i!=bn-1 and b[i]<0 and b[i]*b[i+1]>=0:
        res += b[i]*b[i+1]
        i += 1
    elif i!=bn-1 and b[i+1]>1:
        res += b[i]*b[i+1]
        i += 1
    else:
        res += b[i]
    i+=1
print(res)