from sys import stdin


input = stdin.readline
# r = [4,
# 1,
# 2,
# 46,
# 0,
# 2,
# 6,
# 3,
# 42,
# 21,
# 18,
# 17,
# 4,
# 4,
# 6,
# 42,
# 29,]
for ____ in range(int(input())):
    n,m=map(int,input().split())
    a=[input().strip() for _ in range(n)]
    d = [[-1]*(1<<m+1) for _ in range(n*m)]
    C = m+1
    LEFT = 0
    LEFT |= (1<<2)
    # LEFT |= (1<<m+2)
    RIGHT = 0
    RIGHT |= (1<<0)
    RIGHT |= (1<<m)
    LR = LEFT|RIGHT

    def dfs(c, cnt, path):
        if c==n*m:
            return cnt
        if c>=n*m:
            return 0
        
        if d[c][path]!=-1:
            return d[c][path]
        d[c][path] = 0

        if a[c//m][c%m]=='x':
            d[c][path]=dfs(c+1,cnt,path>>1)
            return d[c][path]
        # left
        elif c%m==0:
            if path&LEFT==0:
                # print('l ', c,c//m,c%m,cnt, bin(path)[2:].zfill(m+2))
                d[c][path]=dfs(c+1,cnt+1,(path>>1)|(1<<(C-1)))
        # right
        elif c%m==m-1:
            if path&RIGHT==0:
                # print('r ', c,c//m,c%m, cnt, bin(path)[2:].zfill(m+2))
                d[c][path]=dfs(c+1,cnt+1,(path>>1)|(1<<(C-1)))
        # center
        else:
            if path&LR==0:
                # print('lr', c,c//m,c%m,cnt, bin(path)[2:].zfill(m+1))
                d[c][path]=dfs(c+1,cnt+1,(path>>1)|(1<<(C-1)))
                # print(bin(path))
                # print(bin((path>>1)|(1<<(C-1))))
        # print('su',c,cnt,bin(path))
        d[c][path]=max(dfs(c+1,cnt,path>>1),d[c][path])
        return d[c][path]
    # print(____,r[____],dfs(0,0,0))
    print(dfs(0,0,0))
# print(LEFT,bin(LEFT))
# print(RIGHT,bin(RIGHT))
# print(LR, bin(LR))