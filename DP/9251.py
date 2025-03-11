lst1 = list(input())
lst2 = list(input())
dp = [[0 for _ in range(len(lst2)+1)] for _ in range(len(lst1)+1)]
for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i] == lst2[j]: dp[i+1][j+1] = dp[i][j]+1
        else: dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

print(dp[len(lst1)][len(lst2)])
