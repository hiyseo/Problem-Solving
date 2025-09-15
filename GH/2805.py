### 수도코드 ###
# (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
# 우선 N 내림차순 정렬 O(NlogN)
# 새로운 리스트 선언(N) - 해당 리스트의 인덱스를 기준으로 잘랐을 때 누적합
# 만약 리스트에 정확히 M이 있다면, 해당 인덱스 반환
# 없다면, M-(작은 인덱스에 해당하는 값) // 해당 인덱스

N, M = map(int, input().split())

trees = list(map(int, input().split()))
sum_t = [0 for _ in range(N)]
found = False
res = 0

trees.sort(reverse = True)
for i in range(1, N):
    gap = trees[i-1] - trees[i]
    sum_t[i] = sum_t[i-1] + gap*i

for i in range(1, N):
    if sum_t[i] == M:
        res = trees[i]
        found = True
        break
    if sum_t[i] > M:
        rest_t = M - sum_t[i-1]
        if rest_t%i == 0:
            cal = rest_t//i
        else:
            cal = rest_t//i+1
        res = trees[i-1] - cal
        found = True
        break

if not found:
    rest_t = M - sum_t[N-1]
    if rest_t%N == 0:
            cal = rest_t//N
    else:
        cal = rest_t//N + 1
    res = trees[N-1] - cal

print(res)
