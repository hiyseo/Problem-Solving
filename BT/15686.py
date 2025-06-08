# 뭐를 골라야할지 모르니까?
# houses = [tuple(좌표)들의 리스트]
# chickens = [tuple(좌표)들의 리스트]
# visited = [False for _ in range(len(chickens))]
# 자 그러면
# visited가 M개가 되면, 치킨거리 구하기 -> 함수
# 치킨거리는 어떻게 구하냐, houses 각각에 대해서 각 치킨집들의 치킨거리의 최소값들의 합

N, M = map(int, input().split())
# print(f"N: {N}, M: {M}")
houses = []
chickens = []
min_val = float('inf')

for i in range(N):
    lst = list(map(int, input().split()))
    for j in range(len(lst)):
        if lst[j] == 1: houses.append((i, j))
        elif lst[j] == 2: chickens.append((i, j))

# visited = [False for _ in range(len(chickens))]
# print(f"houses: {houses}")
# print(f"chickens: {chickens}")
# print(f"visited: {visited}")

def chicken_distance(house, chicken):
    return abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])

# def search(count, selected):
#     global min_val
#     # print(f"count: {count}, selected: {selected}")
#     if count == M:
#         # print(f"REACHED COUNT {M}!!")
#         val = 0
#         for house in houses:
#             tmp = []
#             for chicken in selected:
#                 tmp.append(chicken_distance(house, chicken)) #집과 치킨집의 단순 거리 계산
#             val += min(tmp)
#         # print(f"val: {val}")
#         min_val = min_val if min_val < val else val
#         # if min_val == val: print(f"MIN_VAL CHANGE TO {min_val}")
#         return
#     for i in range(len(chickens)):
#         if not visited[i]:
#             visited[i] = True
#             selected.append(chickens[i])
#             search(count+1, selected)
#             visited[i] = False
#             selected.pop()

def search(start, count, selected):
    global min_val
    if count == M:
        val = 0
        for house in houses:
            val += min([chicken_distance(house, c) for c in selected])
        min_val = min(min_val, val)
        return

    for i in range(start, len(chickens)):
        selected.append(chickens[i])
        search(i + 1, count + 1, selected)
        selected.pop()

search(0, 0, [])
print(f"min_val: {min_val}")

# input
# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

# output
# 5

# input
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2

# output
# 10

# input
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0

# output
# 11

# input
# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1

# output
# 32
