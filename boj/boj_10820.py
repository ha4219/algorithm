from sys import stdin,maxsize


input = stdin.readline
a=ord('a')
z=ord('z')
A=ord('A')
Z=ord('Z')
def f(s):
    r = [0] * 4
    sl = len(s)

    for i in range(sl):
        c = s[i]
        if c.isspace():
            r[3]+=1
        elif c.islower():
            r[0]+=1
        elif c.isupper():
            r[1]+=1
        elif c.isdigit():
            r[2]+=1
    return r

while True:
    try:
        s=input()
        if not s:
            break
        print(*f(s[:-1]))
    except:
        break