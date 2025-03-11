from collections import deque

N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]
people =  [False for _ in range(N+1)] # 진실을 아는 사람들
parties, connected = [], [[] for i in range(N+1)]
answer = M
for _ in range(M):
    parties.append(list(map(int, input().split()))[1:])

for party in parties:
    # print(f"party: {party}")
    for i in range(len(party)):
        for j in range(len(party)):
            if party[i] == party[j]: continue
            else: connected[party[i]].append(party[j])

queue = deque()
for i in truth:
    queue.append(i)

# print(f"connected: {connected}")
# print(f"queue: {queue}")

while queue:
    curr = queue.popleft()
    # print(f"curr: {curr}")
    people[curr] = True
    for person in connected[curr]:
        if not people[person]:
            queue.append(person)

# print(f"people who know truth: {people}")

for party in parties:
    # print(f"party: {party}")
    for person in party:
        if people[person]: #진실을 아는 사람이면
            answer -= 1
            break

# print(f"answer: {answer}")
print(answer)