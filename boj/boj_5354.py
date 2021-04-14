from sys import stdin



input = stdin.readline

for _ in range(int(input())):
    if _>0:
        print()
    n = int(input())
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print('#',end='')
            else:
                print('J',end='')
        print()
