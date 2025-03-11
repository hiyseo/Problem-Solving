loop = int(input())
for _ in range(loop):
    N = int(input())
    students = list(map(int, input().split()))
    students.insert(0, 0)
    visited = [False for _ in range(N+1)]
    teammates = 0

    for student in range(1, len(students)):
        cycle = []
        if not visited[student]: #한번도 방문하지 않은 경우
            while True:
                # print(f"student: {student} VISITED!!")
                visited[student] = True
                cycle.append(student)
                next_student = students[student]
                if visited[next_student]: #다른 사람이 이미 방문한 경우
                    if next_student in cycle: #사이클이 존재하는 경우
                        # print("Find CYCLE!!")
                        start_cycle = cycle.index(next_student)
                        teammates += len(cycle[start_cycle:])
                        break
                    else:
                        break
                else: #다른 사람이 처음 방문한 경우
                    student = next_student
    print(N - teammates)