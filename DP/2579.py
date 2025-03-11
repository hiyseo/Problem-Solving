N = int(input())
stairs = []
max_scores = []
for i in range(N):
    s_point = int(input())
    stairs.append(s_point)
    max_scores.append(0)
LEN = len(stairs)-1
if N==1:
    max_scores[0] = stairs[0]
elif N==2:
    max_scores[0] = stairs[0]
    max_scores[1] = stairs[0] + stairs[1]
else:
    max_scores[0] = stairs[0]
    max_scores[1] = stairs[0] + stairs[1]
    #i번째 계단을 밟을 때의 max score
    for i in range(2, LEN+1):
        max_scores[i] = max(max_scores[i-2] + stairs[i], max_scores[i-3]+stairs[i-1]+stairs[i])

# print(f"max_scores: {max_scores}")
print(max_scores[LEN])