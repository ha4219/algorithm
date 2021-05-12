from sys import stdin


input = stdin.readline

while 1:
    a,b,c=map(int,input().split())
    m = max(a,max(b,c))
    if a==b and b==c and c==0:
        break
    if a==b and b==c:
        print('Equilateral')
    elif a+b+c-m<=m:
        print('Invalid')
    elif a==b or b==c or a==c:
        print('Isosceles')
    else:
        print('Scalene')