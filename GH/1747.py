# def is_prime(n) -> int:
# 소수인지 판별하는 함수

# def is_palindrom(n) -> bool:
# 펠린드롬수인지 판별하는 함수
import math

def is_prime(n) -> bool:
    if n==1: return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0: return False
    return True

def is_palindrom(n) -> bool:
    lst = list(str(n))
    for i in range(len(lst)//2):
        if lst[i] == lst[len(lst)-1-i]: continue
        else: return False
    return True


N = int(input())
# print(f"is_prime({N}): {is_prime(N)}")

while True:
    # print(f"N: {N}")
    if is_prime(N) and is_palindrom(N):
        print(N)
        break
    else: N+=1