# 문제
# 숫자 1, 2, 3으로만 이루어지는 수열이 있다. 임의의 길이의 인접한 두 개의 부분 수열이 동일한 것이 있으면, 그 수열을 나쁜 수열이라고 부른다. 그렇지 않은 수열은 좋은 수열이다.

# 다음은 나쁜 수열의 예이다.

# 33
# 32121323
# 123123213
# 다음은 좋은 수열의 예이다.

# 2
# 32
# 32123
# 1232123
# 길이가 N인 좋은 수열들을 N자리의 정수로 보아 그중 가장 작은 수를 나타내는 수열을 구하는 프로그램을 작성하라. 
# 예를 들면, 1213121과 2123212는 모두 좋은 수열이지만 그 중에서 작은 수를 나타내는 수열은 1213121이다.

# 입력
# 입력은 숫자 N하나로 이루어진다. N은 1 이상 80 이하이다.

# 출력
# 첫 번째 줄에 1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열만 출력한다. 수열을 이루는 1, 2, 3들 사이에는 빈칸을 두지 않는다.

# 예제 입력 1 
# 7
# 예제 출력 1 
# 1213121

def check(s: str) -> bool:
    """
    문자열 s를 입력으로 받아서, 좋은 수열인지(True) 나쁜 수열인지(False) 판별
    """
    L = len(s)
    check_len = L // 2
    if check_len >= 1:
        for i in range(1, check_len+1):
            # L = 5라면, check_len = 2이고, i = 1, 2
            k = L-i # k = 4, 3
            if s[k:] == s[2*k-L:k]: return False
        return True
    else: return True

def add_str(s: str) -> str:
    """
    빈 문자열에서 시작하여, 좋은 수열인 경우 문자열을 계속 확장
    """
    if len(s) == N: return s
    for num in nums:
        if check(s+num):
            result = add_str(s+num)
            if result: return result

nums = ['1', '2', '3']
res = ''
N = int(input())
res = add_str(res)
print(res)