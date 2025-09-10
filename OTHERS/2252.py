from collections import deque

N, M = map(int, input().split())
indegree = [0 for _ in range(N+1)]
orders = [[] for _ in range(N+1)]
queue = deque()

for _ in range(M): #O(M)
    a, b = map(int, input().split())
    indegree[b] += 1
    orders[a].append(b)

for i in range(1, N+1): #O(N)
    if indegree[i] == 0:
        queue.append(i)

# print(f"first queue: {queue}")
# print(f"indegree: {indegree}")
# print(f"orders: {orders}")

cnt = 0

while queue:
    # print(f"queue: {queue}")
    curr = queue.popleft()
    if cnt == N-1: print(curr)
    else: print(curr, end=' ')

    for num in orders[curr]:
        # print(f"num: {num}")
        indegree[num]-=1

        if indegree[num] == 0:
            queue.append(num)
    
    cnt+=1