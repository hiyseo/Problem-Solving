# 입력
# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 
# 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 
# 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 
# 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 
# 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.


### 수도코드 ###
# 트리 임의의 노드에서 가장 먼 노드를 찾는다.
# 그 노드에서 다시 가장 먼 노드를 찾는다.
# 시간복잡도: O(n)

from collections import deque

def find_mx(start, cost):
    queue.append((start, cost))
    mx_start, mx_cost = 0, float('-inf')

    while queue:
        curr, tc = queue.popleft()
        if tc >= mx_cost:
            mx_start = curr
            mx_cost = tc
        
        visited[curr] = True
        for next, cost in nodes[curr]:
            if not visited[next]:
                queue.append((next, tc+cost))
    
    return mx_start, mx_cost

queue = deque()
nodes = {}
n = int(input())
visited = [False for _ in range(n+1)]

for i in range(1, n+1):
    nodes[i] = []

for _ in range(n-1):
    start, end, cost = map(int, input().split())
    nodes[start].append((end, cost))
    nodes[end].append((start, cost))

# 임의의 노드에서 가장 먼 노드 구하기
first_start = 1
total_cost = 0
mx_start, mx_cost = find_mx(first_start, total_cost)

# 트리 지름 구하기
visited = [False for _ in range(n+1)]
second_start = mx_start
total_cost = 0
_, mx_cost = find_mx(second_start, total_cost)
print(mx_cost)



### 테스트 케이스 1 ###
# 6
# 1 2 3
# 1 3 2
# 2 4 5
# 3 6 4
# 3 5 11
# 답: 21

### 테스트 케이스 2 ###
# 6
# 1 2 3
# 1 3 2
# 2 4 5
# 3 6 12
# 3 5 11
# 답: 23

### 테스트 케이스 3 ###
# 12
# 1 2 3
# 1 3 2
# 2 4 5
# 3 5 11
# 3 6 9
# 4 7 1
# 4 8 7
# 5 9 15
# 5 10 4
# 6 11 6
# 6 12 10
# 답: 45