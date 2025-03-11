from collections import deque

queue = deque()
N = int(input())
queue.append((N, 0))
while True:
    current = queue.popleft()
    num, count = current[0], current[1]
    if num==1:
        print(count)
        break
    queue.append((num-1, count+1))
    if num%3==0: queue.append((num//3, count+1))
    if num%2==0: queue.append((num//2, count+1))