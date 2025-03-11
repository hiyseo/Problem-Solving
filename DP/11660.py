N, M = map(int, input().split())
MAT = []
DP = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    lst = list(map(int, input().split()))
    MAT.append(lst)

# DP에 모든 구간합 저장
for x in range(1, N+1):
    for y in range(1, N+1):
        DP[x][y] = MAT[x-1][y-1] + DP[x][y-1] + DP[x-1][y] - DP[x-1][y-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    sum = DP[x2][y2] - DP[x2][y1-1] - DP[x1-1][y2] + DP[x1-1][y1-1]
    print(sum)