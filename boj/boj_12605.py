from sys import stdin

input = stdin.readline

for i in range(int(input())):
    s = list(input().split())
    a = []

    for ss in s:
        a.append(ss)
    print('Case #{}: '.format(i+1)+' '.join(map(str,a[::-1])))