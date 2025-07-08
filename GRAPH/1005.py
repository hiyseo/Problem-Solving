from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    # print(f"N: {N}, K: {K}")

    costs = list(map(int, input().split()))
    costs.insert(0, -1)
    # print(f"costs: {costs}")

    forward_graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        before, after = map(int, input().split())
        forward_graph[before].append(after)
        indegree[after] += 1
    # print(f"forward_graph: {forward_graph}")
    # print(f"indegree: {indegree}")

    target = int(input())

    dq = deque()
    dp = [ 0 for i in range(N+1)]
    for i in range(1, N+1):
        if indegree[i]==0:
            dp[i] = costs[i]
            dq.append(i)
    

    while dq:
        # print(f"dq: {dq}")
        curr = dq.popleft()
        for next in forward_graph[curr]:
            dp[next] = max(costs[next]+dp[curr], dp[next])
            indegree[next]-=1
            if indegree[next] == 0:
                dq.append(next)

        if indegree[target] == 0:
            print(dp[target])
            break