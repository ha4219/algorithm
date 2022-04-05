N = 1000
MAX = 100000

print(N)
a = [[MAX] * N for _ in range(N)]
for i in a:
    print(*i)

rc = [[1, 2], [1, 3], [1, 5]]

# print(len(rc))
# for i in rc:
#     print(*rc)
# print(23)
# for i in range(1, N+1):
#     for j in range(1, N+1):
#         if i == j and (i == 1 or j == N):
#             continue
#         print(i, j)
