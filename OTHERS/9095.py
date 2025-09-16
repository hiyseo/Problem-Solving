### 수도코드 ##
# DFS(재귀)
# DP

### DFS ###
NUMS = [1, 2, 3]

def count(n, cur):
    if cur == n:
        return 1
    elif cur > n:
        return 0
    total = 0 # 로컬 결과
    for num in NUMS:
        total += count(n, cur + num)
    return total # 부모에 결과 전달
    
T = int(input())
for _ in range(T):
    N = int(input())
    print(count(N, 0))


### DP ###
dp = [0 for _ in range(12)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 12):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])