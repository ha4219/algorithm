from sys import stdin


input = stdin.readline

a,b=map(int,input().split())
am = 4 if a%4==0 else a%4
bm = 4 if b%4==0 else b%4
ad = a//4-1 if a%4==0 else a//4
bd = b//4-1 if b%4==0 else b//4
# print(am,bm, ad, bd)
print(abs(am-bm)+abs(ad-bd))