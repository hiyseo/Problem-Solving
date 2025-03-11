#대문자로 변경
text = list(input().upper())
my_dict = {}
max = 0
max_key = []
for letter in text:
    if letter not in my_dict:
        my_dict[letter]=1
    else:
        my_dict[letter]+=1

# print(my_dict)

for key in my_dict:
    if my_dict[key]>max:
        max = my_dict[key]

for key in my_dict:
    if my_dict[key] == max:
        max_key.append(key)

if len(max_key)>1:
    print("?")
else:
    print(max_key[0])