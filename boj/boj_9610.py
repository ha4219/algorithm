from sys import stdin


input = stdin.readline

n=int(input())
a = [0]*5
for _ in range(n):
    x,y=map(int,input().split())
    if x==0 or y==0:
        a[4] += 1
    elif x>0 and y>0:
        a[0] += 1
    elif x>0 and y<0:
        a[3] += 1
    elif x<0 and y>0:
        a[1] += 1
    else:
        a[2] += 1
print('Q1:',a[0])
print('Q2:',a[1])
print('Q3:',a[2])
print('Q4:',a[3])
print('AXIS:',a[4])