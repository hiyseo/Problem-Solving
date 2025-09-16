N, M = map(int, input().split())
K = list(map(int, input().split()))

ans = 0

def search(cur: int):
    global ans
    if cur > N:
        return
    if cur > ans:
        ans = cur
    for d in K:
        search(cur*10 + d)

search(0)
print(ans)

### 테스트케이스 ###
# 657 3
# 1 5 7