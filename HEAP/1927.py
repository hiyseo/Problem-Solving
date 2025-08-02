### 수도코드 ###
# 배열이 비어있다면 그냥 추가
# 배열에 숫자가 존재한다면, 해당 숫자 왼쪽에 삽입

# lst = []

# N = int(input())
# for _ in range(N):
#     n = int(input())
#     if n == 0:
#         if lst:
#             print(lst[0])
#             del lst[0]
#         else: print(0)
#     else:
#         if lst:
#             i = 0
#             while i < len(lst):
#                 if n < lst[i]:
#                     i+=1
#                 else: break
#             lst.insert(i, n)
#         else:
#             lst.append(n)

import heapq
import sys

input = sys.stdin.readline
heap = []

N = int(input())
for _ in range(N):
    n = int(input())
    if n == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, n)

