x = int(raw_input())
my_list = [False for i in range(0,1000001)]
for num in range(0,x):
    my_list[int(raw_input())] = True
for i in range(0,1000001):
    if my_list[i] == True:
        print(i)