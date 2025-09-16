### 수도코드 ###
# LCS 문제 -> DP
# 1번 문자열(i), 2번 문자열(j)로 각각 비교
# dp[i][j]로 i번째, j번째 고려한 최장거리를 memorization
# 시간복잡도: O(N^2)

str1 = list(input())
str2 = list(input())
l1, l2 = len(str1), len(str2)
dp = [[[0, ""] for _ in range(l2+1)] for _ in range(l1+1)] # 리스트(길이, 문자열)로 저장

for i in range(1, l1+1):
    for j in range(1, l2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j][0] = dp[i-1][j-1][0]+1
            dp[i][j][1] = dp[i-1][j-1][1]+str1[i-1]
        else:
            dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0])
            dp[i][j][1] = dp[i-1][j][1] if dp[i-1][j][0] > dp[i][j-1][0] else dp[i][j-1][1]

print(dp[l1][l2][0])
print(dp[l1][l2][1])


### 테스트케이스 ###
# ACAYKP
# CAPCAK