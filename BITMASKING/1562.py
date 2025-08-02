# 문제
# 45656이란 수를 보자.

# 이 수는 인접한 모든 자리의 차이가 1이다. 이런 수를 계단 수라고 한다.

# N이 주어질 때, 길이가 N이면서 0부터 9까지 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. 
# 0으로 시작하는 수는 계단수가 아니다.

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 1

# 힌트
# 참고로, N=1일때부터, N=40일 때 까지 답을 모두 더하면 126461847755이 나온다.


MOD = 1_000_000_000
N = int(input())
# dp[length][last_digit][bitmasking]
dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(N+1)]

for digit in range(1, 10):
    dp[1][digit][(1<<digit)] = 1

for length in range(2, N+1):
    for digit in range(10):
        for mask in range(1<<10):
            if digit > 0:
                dp[length][digit][mask | (1<<digit)] += dp[length-1][digit-1][mask]
                dp[length][digit][mask | (1<<digit)] %= MOD
            if digit < 9:
                dp[length][digit][mask | (1<<digit)] += dp[length-1][digit+1][mask]
                dp[length][digit][mask | (1<<digit)] %= MOD

answer = 0
FULL_MASK = (1<<10) -1
for digit in range(10):
    answer = (answer + dp[N][digit][FULL_MASK])%MOD
print(answer)
