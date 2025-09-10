N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

res = [0, 0, 0]
G_MIN = float('inf')

for i in range(N-2):
    left, right = i+1, N-1
    while left < right:
        s = numbers[i] + numbers[left] + numbers[right]
        if abs(s) < G_MIN:
            G_MIN = abs(s)
            res = [numbers[i], numbers[left], numbers[right]]
        if s < 0:
            left += 1
        elif s > 0:
            right -= 1
        else:  # s == 0
            res = [numbers[i], numbers[left], numbers[right]]
            left = right  # break

print(*res)