n = int(input())
a_list = []

for i in range(n):
    a = input()
    a_list.append(a)

a_list2 = list(set(a_list)) # 집합자료형 set를 사용하여 중복을 제거
a_list3 = [] # 가장 많이 팔린 책을 담을 리스트 
best = 0

for j in range(len(a_list2)): # 가장 많이 팔린 책의 수로 best 초기화 
    if a_list.count(a_list2[j]) >= best:
        best = a_list.count(a_list2[j])

for k in range(len(a_list2)):
    if a_list.count(a_list2[k]) >= best:
        a_list3.append(a_list2[k])

a_list3.sort()
print(a_list3[0])
