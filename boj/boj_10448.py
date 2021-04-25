from sys import stdin


input = stdin.readline

MAX = 1001
d = [0] * MAX
r = [0] * MAX

for i in range(MAX):
    t = i*(i+1)//2
    d[i] = t

for i in range(1,MAX):
    if d[i]>=MAX:
        break
    for j in range(1,MAX):
        if d[i]+d[j]>=MAX:
            break
        for k in range(1,MAX):
            if d[i]+d[j]+d[k]>=MAX:
                break
            r[d[i]+d[j]+d[k]] = 1

for _ in range(int(input())):
    print(r[int(input())])