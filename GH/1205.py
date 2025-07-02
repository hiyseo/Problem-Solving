### 수도코드 ###
# 점수 개수(N), 태수 점수(S), 랭킹리스트 개수(P) 입력
# N==0이라면, 1출력 후 종료
# N>0인 경우에 scores = list(map(int, input().split()))
# target = N
# rank, cnt = 1, 0
# scores의 요소들 돌면서, N보다 크면 rank+=1, cnt+=1
# N과 같으면 작은게 나올때까지 cnt+=1
# 만약 cnt > P라면 rank = -1 출력 후 종료
# N보다 작은게 나오면 rank 출력

N, S, P = map(int, input().split())
# print(f"N: {N}, S: {S}, P: {P}")
if N==0: rank = 1
else:
    scores = list(map(int, input().split()))
    # print(f"scores: {scores}")
    target = S
    rank, cnt = 1, 0
    while True:
        # print(f"rank: {rank}, cnt: {cnt}")
        if cnt >= P and cnt>=N:
            rank = -1
            break
        elif cnt < P and cnt>=N:
            break
        curr = scores[cnt]
        if curr > target:
            rank+=1
            cnt+=1
        elif curr == target:
            cnt+=1
        else: break

print(rank)


### 테스트케이스 ###
# 5 50 6
# 100 90 50 50 50

# rank: 3