from sys import stdin

input = stdin.readline

s = input().strip()
sl = len(s)
sign = []
a = []

for i in range(sl):
    if s[i].isdigit():
        a.append(int(s[i]))
    else:
        q = a.pop()
        p = a.pop()
        if s[i]=='+':
            a.append(p+q)
        elif s[i]=='-':
            a.append(p-q)
        elif s[i]=='*':
            a.append(p*q)
        else:
            a.append(p/q)
print(a[0])