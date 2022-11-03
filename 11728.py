a, b = map(int, input().split())

num_list1 = list(map(int, input().split()))

num_list2 = list(map(int, input().split()))

num_list3 = num_list1 + num_list2
num_list3.sort()

for i in num_list3:
    print(i, end='')
