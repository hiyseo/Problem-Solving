# 기존 모드의 시간복잡도 O(N*K)

### 수도코드 ###
# 가방 무게 오름차순 O(KlogK)
# 보석 무게 기준 오름차순 O(NlogN)
# 가방 무게보다 가벼운 보석들 heapq에 넣고 pop

import heapq

N, K = map(int, input().split())
jewerls, bags = [], []
total = 0

for _ in range(N):
    M, V = map(int, input().split())
    jewerls.append((M, V))

for _ in range(K):
    C = int(input())
    bags.append(C)

jewerls.sort(key = lambda x: x[0])
bags.sort()

hq = []
i = 0
for b_weight in bags:
    while i<N and jewerls[i][0] <= b_weight:
        heapq.heappush(hq, (-jewerls[i][1], jewerls[i][0]))
        i+=1
    if hq:
        cost, weight =  heapq.heappop(hq)
        cost = -cost
        total+=cost

print(total)

# 예제 입력 1 
# 2 1
# 5 10
# 100 100
# 11
# 예제 출력 1 
# 10

# 예제 입력 2 
# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2
# 예제 출력 2 
# 164

# 예제 입력 2 
# 3 2
# 9 65
# 5 23
# 1 99
# 10
# 2
# 예제 출력 2 
# 164