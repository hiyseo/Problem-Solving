### 수도코드 ###
# dp 선언
# 해당 스티커를 뗀 경우, 얻을 수 있는 최대값 dp에 저장
# 어떤 칸을 떼었다고 가정하면,
# 이전 칸의 다른 칸 or 이이전 칸의 같은 칸 비교하기!

T = int(input())
for _ in range(T):
    n = int(input())
    numbers = [] # numbers 입력

    dp = [[ 0 for _ in range(n)] for _ in range(2)]
    for _ in range(2):
        numbers.append(list(map(int, input().split())))
    
    for j in range(n):
        if j==0: # 처음 시작하는 값은 그대로 저장
            dp[0][j], dp[1][j] = numbers[0][j], numbers[1][j]
        elif j==1: # 첫 번째 칸 - 대각선
            dp[0][j] = dp[1][0]+numbers[0][j]
            dp[1][j] = dp[0][0]+numbers[1][j]
        else: # 두 번째 칸 이상 - 대각선 or 2칸 전의 같은 칸
            for i in range(2):
                new_i = abs(i-1) # i=0 이면 new_i=1, i=1이면 new_i=0
                dp[i][j] = numbers[i][j] + max(dp[new_i][j-1], dp[new_i][j-2])
    
    print(max(dp[0][n-1], dp[1][n-1]))
            


# input
# 2
# 5
# 50 10 100 20 40
# 30 50 70 10 60
# 7
# 10 30 10 50 100 20 40
# 20 40 30 50 60 20 80

# output
# 260
# 290