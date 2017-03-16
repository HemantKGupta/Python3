x = int(raw_input())
my_list = []
for num in range(x):
    my_list.append(int(raw_input()))
my_list.sort()
for val in my_list:
    print(val)