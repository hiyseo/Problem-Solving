# 숫자들을 스택(리스트)에 저장 -> 순서 변하지 X
# 연산자의 조합 -> how??, 
# 스택에서 숫자 두개 꺼낸 후 가장 최상의 연산자와 계산 후 스택에 쌓음
# 사용된 연산자는 pop
# 모든 연산자의 조합에 대해서 결과값 계산 후 결과(answer) 리스트에 저장
# 최대값, 최소값 출력

N = int(input())
numbers = list(map(int, input().split()))
add, min, mul, div = map(int, input().split())
# print(f"numbers: {numbers}")
# print(f"add: {add}, min: {min}, mul: {mul}, div: {div}")

max_val, min_val = -10**9, 10**9

def backtrack(index, cur_val, add, min, mul, div) -> int:
    global max_val, min_val
    # print(f"index: {index}")
    if index == N-1:
        max_val = max_val if max_val > cur_val else cur_val
        min_val = min_val if min_val < cur_val else cur_val
        # print(f"max_val: {max_val}, min_val: {min_val}")

    if add > 0:
        backtrack(index+1, cur_val+numbers[index+1], add-1, min, mul, div)
    if min > 0:
        backtrack(index+1, cur_val-numbers[index+1], add, min-1, mul, div)
    if mul > 0:
        backtrack(index+1, cur_val*numbers[index+1], add, min, mul-1, div)
    if div > 0:
        if cur_val < 0:
            backtrack(index+1, -(-cur_val//numbers[index+1]), add ,min, mul, div-1)
        else:
            backtrack(index+1, cur_val//numbers[index+1], add, min, mul, div-1)

backtrack(0, numbers[0], add, min, mul, div)
print(max_val)
print(min_val)