# 수도코드
# 전체 수열이 있을 때, 부분 수열이 팰린드롬인지 아닌지 확인하는 방법
# 수열 크기 (1 <= N <= 2000), 질문 개수 (1 ≤ M ≤ 1,000,000)
# is_pal[i][j] - i부터 j까지의 수열이 팰린드롬인지 아닌지 저장하는 DP
# is_pal[i][j] = 전체수열[i] == 전체수열[j] && is_pal[i+1][j-1]이 팰린드롬이면 됨

# from pprint import pprint

import sys
input = sys.stdin.readline
# write = sys.stdout.write

N = int(input())
is_pal = [[0 for _ in range(N+1)] for _ in range(N+1)] # 앞의 숫자는 인덱스 맞추기 위한 용도
numbers = list(map(int, input().split()))
# print(f"numbers: {numbers}")

for l in range(1, N+1): # 길이 기준 (우선)
    for i in range(1, N+2-l): # 시작점
        j = l+i-1 # 끝점
        ni, nj = i-1, j-1
        # print(f"l: {l}, i: {i}, j: {j}")
        if l == 1: # 길이가 1일 때 -> 무조건 팰린드롬
            is_pal[i][j] = 1
        elif l == 2: # 길이가 2일때 -> numbers[i]==numberes[j]
            if numbers[ni] == numbers[nj]: is_pal[i][j] = 1
        else: # 길이가 3이상일때 -> numbers[i]==numberes[j] && is_pal[i+1][j-1]==1
            if numbers[ni] == numbers[nj] and is_pal[i+1][j-1] == 1:
                is_pal[i][j] = 1


# pprint(is_pal)

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(is_pal[s][e])
    


