L, C = map(int, input().split())
letters = list(input().split())
letters.sort()
# print(f"letters: {letters}")
vowels = ['a', 'e', 'i', 'o', 'u']

def encrypt(start, path):
    if len(path) == L:
        vowel_count = 0
        for ch in path:
            if ch in vowels: vowel_count+=1
        consonant_count = L - vowel_count
        # print(f"vowel_count: {vowel_count}, consonant_count: {consonant_count}")
        if vowel_count >=1 and consonant_count >=2:
            print(''.join(path))

    for i in range(start, C):
        path.append(letters[i])
        encrypt(i+1, path) # 현재 선택한 알파벳보다 뒤에 있는 알파벳 선택
        path.pop()

encrypt(0, [])