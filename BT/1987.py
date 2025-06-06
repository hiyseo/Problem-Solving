R, C = map(int, input().split())
alps = [list(input().strip()) for _ in range(R)]
visited = set()
# print(f"alps: {alps}")
max_count = float('-inf')
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def search(x, y, count):
  # print(f"visited: {visited}")
  global max_count
  max_count = max_count if max_count > count else count
  # if max_count == count: print(f"MAX COUNT CHANGED! -> {max_count}")
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0<=nx<R and 0<=ny<C and alps[nx][ny] not in visited:
      # print(f"{alps[nx][ny]} appended to visited!!")
      visited.add(alps[nx][ny])
      search(nx, ny, count+1)
      visited.remove(alps[nx][ny])

visited.add(alps[0][0])
search(0, 0, 1)
print(max_count)