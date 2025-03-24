# N의 약수를 구하는 함수 호출
# 리스트로 반환 받고
# 리스트에서 K번째 숫자 출력

N, K = map(int, input().split())
# print(f"N: {N}, K: {K}")
answer = []

def find_prime(N)->list:
    for i in range(1, N+1):
        if N%i==0:
            answer.append(i)
    return answer

find_prime(N)
# print(f"answer: {answer}")
if len(answer)<K:
    print(0)
else:
    print(answer[K-1])