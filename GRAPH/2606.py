N = int(input())
M = int(input())
VIRUS = [0 for _ in range(N+1)]
total = 0

# 1번 컴퓨터 감염
VIRUS[1]=1

for _ in range(M):
    a, b = map(int, input().split())
    if VIRUS[a]==1: #만약 a번 컴퓨터가 감염되었다면
        # print(f"{b}번 컴퓨터가 감염되었습니다.")
        VIRUS[b]=1

for computer in VIRUS:
    if computer==1:
        total+=1

print(total-1)