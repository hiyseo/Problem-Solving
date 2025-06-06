# permutation 함수
# 절대값 계산 함수
# N 입력받은 후 permutation 함수로 가능한 모든 조합 계산
# 이때 절대값을 계산 후 최대값 출력

def calculate(a, b) -> int:
    ret = a-b if a>b else b-a
    return ret

def permutation(path) -> list:
    global max
    if len(path)==N:
        ret = 0
        for i in range(len(path)-1):
            ret += calculate(path[i], path[i+1])
            # print(f"ret: {ret}")
            max = max if max > ret else ret
        # print(path)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            path.append(numbers[i])
            permutation(path)
            path.pop()
            visited[i]=False

max = float('-inf')
N = int(input())
visited = [False for _ in range(N)]
numbers = list(map(int, input().split()))
res = []
total = []
permutation(res)
# print(f"max: {max}")
print(max)