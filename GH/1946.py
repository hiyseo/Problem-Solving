T = int(input())
for _ in range(T):
    N = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(N)]
    scores.sort()

    selected_count = 0
    min_meet = float('inf')

    for doc, meet in scores:
        if meet < min_meet:
            selected_count += 1
            min_meet = meet

    print(selected_count)