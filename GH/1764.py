# 문제
# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. 
# N, M은 500,000 이하의 자연수이다.

# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

# 출력
# 듣보잡의 수와 그 명단을 사전순으로 출력한다.

# 예제 입력 1 
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton

# 예제 출력 1 
# 2
# baesangwook
# ohhenrie

### 풀이방법 ###
# 1. 리스트 이용 - 리스트 추가 후 검색 O(N*M)
# 2. set 이용 - hash 기반이라 검색 O(1), 다만 메모리,,?

### 수도코드 ###
# 듣도 못한 사람(N) 입력, 보도 못한 사람(M) 입력
# people = set()
# res = []
# N 줄에 걸쳐 people.add(input().strip())
# M 줄에 걸쳐 person = input().strip()
# if person in people: res.append(person)
# res 길이 및 내용 출력

N, M = map(int, input().split())
people = set()
res = []
for _ in range(N):
    people.add(input().strip())
# print(f"people: {people}")
for _ in range(M):
    person = input().strip()
    if person in people: res.append(person)
print(len(res))
for db_person in sorted(res):
    print(db_person)