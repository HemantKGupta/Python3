from collections import Counter
mn = input()
m_n = mn.split(' ')
m = int(m_n[0])
n = int(m_n[1])
input_array = input()
input_array_list = input_array.split(' ')
input_array_set = set(input_array_list)

like_set = input()
input_like_set = set(like_set.split(' '))

dislike_set = input()
input_dislike_set = set(dislike_set.split(' '))

result = 0
like_inter = input_array_set.intersection(input_like_set)
dislike_inter = input_array_set.intersection(input_dislike_set)

c=Counter(input_array_list)
for item in like_inter:
    result += c[str(item)]

for item in dislike_inter:
    result -= c[str(item)]

print(result)