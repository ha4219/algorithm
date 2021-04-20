from sys import stdin


input = stdin.readline

s=input().strip()
a = [0] * 3
a[0] = 1
for c in s:
    if c=='A':
        a[0],a[1]=a[1],a[0]
    elif c=='B':
        a[1],a[2]=a[2],a[1]
    elif c=='C':
        a[0],a[2]=a[2],a[0]
print(a.index(1)+1)